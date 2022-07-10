import uuid
from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


# model for post
class Questions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    question = models.TextField(default="")
    address = models.TextField(default="")
    title = models.TextField(default="")

    def __str__(self):
        return self.user
