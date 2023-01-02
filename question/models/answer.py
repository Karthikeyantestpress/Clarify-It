from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel

from .question import Question


class Answer(TimeStampedModel):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="question"
    )
    description = models.TextField()
    answered_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="answerer"
    )

    def __str__(self):
        return f"Answered by {self.answered_by} on {self.question}"
