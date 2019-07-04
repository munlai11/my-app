from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.author.username