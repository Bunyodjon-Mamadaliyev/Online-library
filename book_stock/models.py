from django.db import models

class BookAvailability(models.Model):
    book = models.OneToOneField('books.Book', on_delete=models.CASCADE, related_name='availability')
    status = models.CharField(
        max_length=20,
        choices=[
            ('available', 'Available'),
            ('borrowed', 'Borrowed'),
            ('reserved', 'Reserved')
        ],
        default='available'
    )
    quantity = models.PositiveIntegerField(default=1)
    available_from = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} - {self.status} ({self.quantity})"

