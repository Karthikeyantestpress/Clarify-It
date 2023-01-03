from django.contrib import admin

from question.models.question import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created")
    list_filter = (
        "created_by",
        "created",
    )
    search_fields = ("title", "description")
    raw_id_fields = ("created_by",)
    date_hierarchy = "created"
    ordering = ("created", "created_by")
