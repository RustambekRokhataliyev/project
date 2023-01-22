from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "avatar", "password1", "password2"]


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]
