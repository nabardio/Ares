from django.forms import ModelForm, FileField, FileInput
from django.utils.translation import ugettext_lazy as _
from .models import Robot


class LeagueRegistrationForm(ModelForm):
    class Meta:
        model = Robot
        fields = ('code',)

    code = FileField(label=_('Code'),
                     widget=FileInput,
                     help_text=_('The code of robot you want to register'))
