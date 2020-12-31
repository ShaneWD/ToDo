from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=24)
    completed = models.BooleanField(default=False)
    notes = models.CharField(max_length=80)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.title