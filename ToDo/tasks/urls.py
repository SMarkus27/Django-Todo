from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_tasks),
    path("submit/", views.create_task),
    path('edit/',views.edit_task),
    path('edit/submit/',views.submit_edit),
    path('delete/<id>', views.delete_task),
]