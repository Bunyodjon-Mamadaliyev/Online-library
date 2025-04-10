from django.contrib import admin
from .models import BookAvailability

@admin.register(BookAvailability)
class BookAvailabilityAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "quantity", "available_from")
    list_filter = ("status", "available_from")
    search_fields = ("book__title",)
    ordering = ("book", "status")
