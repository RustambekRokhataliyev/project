from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # класс для отображения данных о пользователе для django
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
