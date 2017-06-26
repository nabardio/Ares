import sys

import game
import robot1
import robot2


def run(robot1_id, robot2_id):
    game_class = getattr(game, game.__target__)
    robot1_class = getattr(robot1, robot1.__target__)
    robot2_class = getattr(robot2, robot2.__target__)

    game_class(robot1_class(robot1_id), robot2_class(robot2_id)).run()


if __name__ == '__main__':
    run(*sys.argv[1:])
