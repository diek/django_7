from django.contrib import admin
from polls.models import Choice, Question


class ChoiceInLine(admin.StackedInLine):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]

admin.site.register(Question, QuestionAdmin)
