from modeltranslation.translator import register, TranslationOptions
from .models import BookAvailability

@register(BookAvailability)
class BookAvailabilityTranslationOptions(TranslationOptions):
    fields = ('book',)
