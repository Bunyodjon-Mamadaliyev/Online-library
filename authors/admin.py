from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date", "death_date", "slug", "created_at", "updated_at")
    search_fields = ("first_name", "last_name", "slug")
    prepopulated_fields = {"slug": ("first_name", "last_name")}
    list_filter = ("birth_date", "death_date", "created_at", "updated_at")
    ordering = ("last_name", "first_name")

