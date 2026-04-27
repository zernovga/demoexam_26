from django.contrib.auth.views import LoginView
from django.shortcuts import render  # noqa: F401

# Create your views here.


class UserLoginView(LoginView):
    template_name = "core/login.html"
