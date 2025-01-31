from django.db import models
from datetime import date

class Day(models.Model):
    birth_date = models.DateField()

    def __str__(self):
        return self.birth_date.strftime

    @property
    def days_since_birth(self):
        today = date.today()
        delta = today - self.birth_date
        return delta.days


class TextConversion(models.Model):
    latin_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.latin_text[:50]  # Matnning birinchi 50 belgisini ko'rsatish

    @property
    def cyrillic_text(self):
        
        from .services import TextService
        return TextService.convert_to_cyrillic(self.latin_text)