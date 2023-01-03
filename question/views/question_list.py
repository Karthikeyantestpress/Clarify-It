from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from question.models.question import Question


class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = "question/question_list.html"
