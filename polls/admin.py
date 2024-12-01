from django.contrib import admin
from .models import Question, Choise

class ChoiseInline(admin.TabularInline):
    model = Choise
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]})
    ]
    inlines = [ChoiseInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]

admin.site.register(Question, QuestionAdmin)