from modeltranslation.translator import register, TranslationOptions
from .models import Author

@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')