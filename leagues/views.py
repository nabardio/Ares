# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError

from .forms import LeagueRegistrationForm
from .models import League


class LeagueList(ListView):
    """
    List of the leagues
    """
    model = League
    template_name = 'leagues.html'
    context_object_name = 'leagues'


class LeagueDetail(DetailView):
    """
    League detail view
    """
    model = League
    template_name = 'league.html'
    context_object_name = 'league'

    def get_context_data(self, **kwargs):
        """
        Manipulating template context 
        """
        ctx = super(LeagueDetail, self).get_context_data(**kwargs)
        today = timezone.localdate()
        ctx['is_registered'] = False
        ctx['is_expired'] = False
        ctx['is_full'] = self.object.robots.count() == self.object.num_robots
        if self.request.user.is_authenticated():
            ctx['is_registered'] = self.object.robots.filter(
                user=self.request.user).count() > 0
        if today > self.object.registration_date_end or \
                today < self.object.registration_date_start:
            ctx['is_expired'] = True
        return ctx


@method_decorator(login_required, name='dispatch')
class LeagueRegister(UpdateView):
    """
    Registration of a robot in a league
    """
    model = League
    form_class = LeagueRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('leagues:list')
    context_object_name = 'league'

    def get_form(self, form_class=None):
        """
        Manipulating the form
        """
        form = super(LeagueRegister, self).get_form(form_class)
        form.fields['robots'].queryset = self.request.user.robots.all()

        return form

    def form_valid(self, form):
        """
        Form validation
        """
        today = timezone.localdate()
        if today > self.object.registration_date_end or \
                today < self.object.registration_date_start:
            form.add_error(None, ValidationError(
                u'The league registration is expired'))
            return super(LeagueRegister, self).form_invalid(form)
        if self.object.robots.count() == self.object.num_robots:
            form.add_error(None, ValidationError(u'The leagues is full'))
            return super(LeagueRegister, self).form_invalid(form)
        if self.object.robots.filter(user=self.request.user):
            form.add_error(None, ValidationError(u'Already Registered'))
            return super(LeagueRegister, self).form_invalid(form)
        self.object.robots.add(form.cleaned_data['robots'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
