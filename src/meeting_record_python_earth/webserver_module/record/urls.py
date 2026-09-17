from django.urls import path, URLPattern, URLResolver

from . import views

urlpatterns: list[URLResolver | URLPattern] = []