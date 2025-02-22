from django.db import models
from django.core.exceptions import ValidationError

class Quote(models.Model):
    # Primary key is automatically created as 'id'
    text = models.TextField(max_length=500, blank=False)  # The quote text
    author = models.CharField(max_length=100)              # Author of the quote
    source = models.CharField(max_length=100, blank=True)  # Source of the quote (optional)
    year = models.PositiveIntegerField()                    # Year of the quote
    created_at = models.DateTimeField(auto_now_add=True)   # Timestamp when the quote was created
    updated_at = models.DateTimeField(auto_now=True)       # Timestamp when the quote was last updated
    category = models.CharField(max_length=50, blank=True)  # Category of the quote (optional)
    language = models.CharField(max_length=30, default='English')  # Language of the quote
    is_favorite = models.BooleanField(default=False)        # Flag to mark if the quote is a favorite
    tags = models.CharField(max_length=200, blank=True)     # Comma-separated tags for the quote (optional)
    rating = models.FloatField(default=0.0)                 # Rating of the quote (optional)

    def clean(self):
        if len(self.text) < 10:
            raise ValidationError('Quote text must be at least 10 characters long.')

    def __str__(self):
        return f'"{self.text}" - {self.author}'