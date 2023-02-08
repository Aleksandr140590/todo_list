import random
import string

from django.db import models




class Todo(models.Model):
    uuid = models.CharField(max_length=8,
                            unique=True)
    created = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=2000)
    active = models.BooleanField(default=True)