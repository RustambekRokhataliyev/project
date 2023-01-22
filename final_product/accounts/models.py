from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    """Кастомная моделька для пользователя."""

    avatar = models.ImageField(verbose_name="Ава юзера", upload_to="users/avatars/", null=True, blank=True)
