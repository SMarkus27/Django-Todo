from django.contrib import admin
from .models import Tasks


class TasksAdmin(admin.ModelAdmin):
    list_display=('id','task')
admin.site.register(Tasks,TasksAdmin)