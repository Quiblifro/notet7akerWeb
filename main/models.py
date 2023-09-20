from django.db import models
from datetime import datetime
from django.urls import reverse
class User(models.Model):
    name = models.CharField(max_length=150)
    telegram_id = models.IntegerField()



class Note(models.Model):
    content = models.TextField()
    author = models.IntegerField()
    created_at = models.DateTimeField(default = datetime.now)
    updated_at = models.DateTimeField(default = datetime.now)

    def __str__ (self):
        return f'{self.content}'
