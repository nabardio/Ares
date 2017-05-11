from django.views.generic import ListView, DetailView, CreateView
from django.utils import timezone
from django.urls import reverse_lazy
from .models import League
from .forms import LeagueRegistrationForm


class LeagueList(ListView):
    model = League
    template_name = 'leagues.html'
    context_object_name = 'leagues'


class LeagueDetail(DetailView):
    model = League
    template_name = 'league.html'
    context_object_name = 'league'

    def get_context_data(self, **kwargs):
        ctx = super(LeagueDetail, self).get_context_data(**kwargs)
        today = timezone.localdate()
        ctx['is_registered'] = False
        ctx['is_expired'] = False
        if self.request.user.is_authenticated():
            ctx['is_registered'] = self.object.robots.filter(
                user=self.request.user).count() > 0
        if today > self.object.registration_date_end or \
                        today < self.object.registration_date_start:
            ctx['is_expired'] = True
        return ctx


class LeagueRegister(CreateView):
    form_class = LeagueRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('leagues:list')

    def get_context_data(self, **kwargs):
        ctx = super(LeagueRegister, self).get_context_data(**kwargs)
        ctx['league'] = League.objects.get(pk=self.kwargs[self.pk_url_kwarg])
        return ctx
    
    def form_valid(self, form):
        league = League.objects.get(pk=self.kwargs[self.pk_url_kwarg])
        if not league.robots.filter(user=self.request.user):
            form.instance.user = self.request.user
            form.instance.league = league
        return super(LeagueRegister, self).form_valid(form)
