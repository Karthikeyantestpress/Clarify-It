from django.contrib import admin

from question.models.answer import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "answered_by", "created")
    list_filter = (
        "answered_by",
        "created",
    )
    search_fields = ("question", "description")
    raw_id_fields = ("answered_by",)
    date_hierarchy = "created"
    ordering = ("created", "answered_by")
