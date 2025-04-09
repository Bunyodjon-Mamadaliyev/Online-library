from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    authors = models.ManyToManyField('authors.Author')
    categories = models.ManyToManyField('categories.Category')
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    publisher = models.CharField(max_length=200)
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

