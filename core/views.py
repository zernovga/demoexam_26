from django.contrib.auth.views import LoginView
from django.shortcuts import render  # noqa: F401
from django.views.generic import ListView

from .models import Product


class UserLoginView(LoginView):
    template_name = "core/login.html"


class ProductListView(ListView):
    model = Product
    template_name = "core/product_list.html"
    context_object_name = "products"
