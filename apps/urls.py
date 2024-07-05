
from django.contrib import admin
from django.urls import path, include

from apps.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('product/detail/<int>', HomeTemplateView.as_view(), name='product_detail'),
    path('', HomeTemplateView.as_view(), name='home'),
]