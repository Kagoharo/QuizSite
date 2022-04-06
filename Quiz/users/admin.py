from django.contrib import admin

from .models import CustomUser

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#   """
#   Модель категорий для вывода в админ панели.
#   """

#   list_display = ('id', 'category_name', 'created_at')
#   list_display_links = ('id', 'category_name')
#   search_fields = ('category_name',)
#   list_filter = ('created_at',)
