from django.db import models


class Tasks(models.Model):

    task = models.CharField(max_length=150, blank=False)
    
    class Meta:
        verbose_name_plural = 'Tasks'