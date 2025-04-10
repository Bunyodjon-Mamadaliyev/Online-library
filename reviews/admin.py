from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("book", "user_name", "rating", "created_at")
    search_fields = ("book__title", "user_name")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)
