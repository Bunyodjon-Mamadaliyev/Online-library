from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn", "published_date", "publisher", "language", "created_at", "updated_at")
    search_fields = ("title", "isbn", "publisher")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("published_date", "language", "publisher")
    ordering = ("title", "published_date")
    filter_horizontal = ("authors", "categories")
