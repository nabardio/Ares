from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1',
                  'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        print(email, username)
        if email and User.objects.filter(email=email).exists():
            raise ValidationError(
                u'A user with that email address already exists.')
        return email
