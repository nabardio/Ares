# -*- coding: utf-8 -*-
from django import forms

from .models import League


class LeagueRegistrationForm(forms.ModelForm):
    """
    League robot registration form
    """
    robots = forms.ModelChoiceField(League.objects.none())

    class Meta:
        model = League
        fields = ('robots',)
