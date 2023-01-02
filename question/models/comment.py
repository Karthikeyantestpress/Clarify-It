from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel

from .answer import Answer
from .question import Question


class QuestionComment(TimeStampedModel):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="question_comment"
    )
    description = models.TextField()
    commented_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="question_comment_creator"
    )

    def __str__(self):
        return f"Commented by {self.commented_by} on {self.question}"


class AnswerComment(TimeStampedModel):
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, related_name="answer_comment"
    )
    description = models.TextField()
    commented_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="answer_comment_creator"
    )

    def __str__(self):
        return f"Commented by {self.commented_by} on {self.answer}"
