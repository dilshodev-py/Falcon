from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.models import Product


class HomeTemplateView(ListView):
    model = Product
    template_name = 'apps/product-grid.html'
    context_object_name = 'products'
