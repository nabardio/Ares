# -*- coding: utf-8 -*-
import json
import tarfile
import uuid
from io import BytesIO

import docker
import docker.errors
import pika
from celery import shared_task
from django.conf import settings

from .models import Match


def tar(files):
    """
    Create a tar file from the files
    """
    stream = BytesIO()
    archive = tarfile.TarFile(fileobj=stream, mode='w')
    for name in files:
        info = tarfile.TarInfo(name)
        info.size = files[name].size
        archive.addfile(info, files[name])
    archive.close()
    stream.seek(0)
    return stream


@shared_task(name='matches.tasks.run')
def run_match(match_id):
    """
    Run the match inside a docker container and receive the result from 
    rabbitMQ
    """
    match = Match.objects.get(pk=match_id)
    if match.finished:
        return

    queue_id = str(uuid.uuid4())

    client = docker.from_env()
    try:
        container = client.containers.create(
            settings.DOCKER_IMAGE,
            " ".join([str(match.robot1_id), str(match.robot2_id)]),
            environment={
                'BATTLEFIELD_MQ_HOST': settings.MQ_HOST,
                'BATTLEFIELD_MQ_USERNAME': settings.MQ_USERNAME,
                'BATTLEFIELD_MQ_PASSWORD': settings.MQ_PASSWORD,
                'BATTLEFIELD_MQ_VHOST': settings.MQ_VHOST,
                'BATTLEFIELD_MQ_QUEUE': queue_id,
            }
        )
    except (docker.errors.APIError, docker.errors.ImageNotFound) as e:
        print(e)
        return

    try:
        archive = tar({'game.py': match.game.code,
                       'robot1.py': match.robot1.code,
                       'robot2.py': match.robot2.code})
        if not container.put_archive("/game", archive):
            # TODO: handle the errors
            return

        container.start()

    except (docker.errors.APIError, docker.errors.ImageNotFound) as e:
        # TODO: handle the errors
        print(e)
        return
    finally:
        exit_code = container.wait()
        container.remove()
        if exit_code != 0:
            return

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.MQ_HOST,
            virtual_host=settings.MQ_VHOST,
            credentials=pika.PlainCredentials(username=settings.MQ_USERNAME,
                                              password=settings.MQ_PASSWORD)
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue_id)

    steps = []
    for method_frame, props, body in channel.consume(queue=queue_id):
        data = json.loads(body)
        steps.append(data)
        channel.basic_ack(method_frame.delivery_tag)
        if data['step'] == -1:
            match.robot1_score = data['msg'][str(match.robot1_id)]
            match.robot2_score = data['msg'][str(match.robot2_id)]
            break
    channel.cancel()
    channel.queue_delete(queue=queue_id)
    channel.close()
    connection.close()

    match.log = json.dumps(steps)
    match.finished = True
    match.save()

    if match.league.matches.filter(finished=False).count() == 0:
        match.league.finished = True
        match.league.save()
