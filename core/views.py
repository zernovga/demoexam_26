from typing import Any

from django.contrib.auth.views import LoginView
from django.shortcuts import render  # noqa: F401
from django.views.generic import ListView

from .models import Product, Supplier


class UserLoginView(LoginView):
    template_name = "core/login.html"


class ProductListView(ListView):
    model = Product
    template_name = "core/product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["suppliers"] = Supplier.objects.all()
        context["current_supplier"] = self.request.GET.get("supplier", "")

        return context
