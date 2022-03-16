from django.contrib import admin
from .models import *

admin.site.register(Quiz)
admin.site.register(Category)


class AdminAnswer(admin.StackedInline):
    model = Answer


class AdminQuestion(admin.ModelAdmin):
    inlines = [AdminAnswer]


admin.site.register(Question, AdminQuestion)
admin.site.register(Answer)
