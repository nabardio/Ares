# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User


class UserRegistrationForm(UserCreationForm):
    """
    User registration form
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1',
                  'password2')

    def clean_email(self):
        """
        Cleans the email data by checking its existence
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        print(email, username)
        if email and User.objects.filter(email=email).exists():
            raise ValidationError(
                u'A user with that email address already exists.')
        return email
