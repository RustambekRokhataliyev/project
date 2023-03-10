from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("registration/", views.registration_view, name="registration"),
    path("logout/", views.user_logout, name="logout")
]

