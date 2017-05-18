# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, \
    ListView, UpdateView

from .models import Robot


@method_decorator(login_required, name='dispatch')
class UserRobotList(ListView):
    """
    List of user's robots
    """
    model = Robot
    template_name = 'robots.html'
    context_object_name = 'robot'

    def get_queryset(self):
        """
        Limit the query set to only user's robots 
        """
        queryset = super(UserRobotList, self).get_queryset()
        return queryset.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class RobotDetail(DetailView):
    """
    Robot detail view
    """
    model = Robot
    template_name = 'robot.html'
    context_object_name = 'robot'


@method_decorator(login_required, name='dispatch')
class CreateRobot(CreateView):
    """
    Register a new robot
    """
    model = Robot
    fields = ('name', 'code')
    template_name = 'create.html'
    context_object_name = 'robot'
    success_url = reverse_lazy('robots:user-list')

    def form_valid(self, form):
        """
        Manipulating the form
        """
        form.instance.user = self.request.user
        return super(CreateRobot, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditRobot(UpdateView):
    """
    Update a robot
    """
    model = Robot
    fields = ('name', 'code')
    template_name = 'update.html'
    context_object_name = 'robot'
    success_url = reverse_lazy('robots:user-list')

    def get_queryset(self):
        """
        Limit the query set to only user's robots 
        """
        queryset = super(EditRobot, self).get_queryset()
        return queryset.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class DeleteRobot(DeleteView):
    """
    Delete a robot
    """
    model = Robot
    template_name = 'delete.html'
    context_object_name = 'robot'
    success_url = reverse_lazy('robots:user-list')

    def get_queryset(self):
        """
        Limit the query set to only user's robots 
        """
        queryset = super(DeleteRobot, self).get_queryset()
        return queryset.filter(user=self.request.user)
