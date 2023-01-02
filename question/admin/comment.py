from django.contrib import admin

from question.models.comment import AnswerComment, QuestionComment


@admin.register(QuestionComment)
class QuestionCommentAdmin(admin.ModelAdmin):
    list_display = ("question", "commented_by", "created")
    list_filter = (
        "commented_by",
        "created",
    )
    search_fields = ("question", "description")
    raw_id_fields = ("commented_by",)
    date_hierarchy = "created"
    ordering = ("created", "commented_by")


@admin.register(AnswerComment)
class AnswerCommentAdmin(admin.ModelAdmin):
    list_display = ("answer", "commented_by", "created")
    list_filter = (
        "commented_by",
        "created",
    )
    search_fields = ("answer", "description")
    raw_id_fields = ("commented_by",)
    date_hierarchy = "created"
    ordering = ("created", "commented_by")
