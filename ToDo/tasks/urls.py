from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_tasks),
    path("submit/", views.create_tasks),
]