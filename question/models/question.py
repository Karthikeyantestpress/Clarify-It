from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel


class Question(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
