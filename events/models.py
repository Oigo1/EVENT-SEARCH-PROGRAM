from django.db import models

# Create your models here.

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('wedding', 'Wedding'),
        ('party', 'Party'),
        ('club', 'Club Event'),
        ('government', 'Government Event'),
        ('conference', 'Conference'),
        ('concert', 'Concert'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(null=True, blank=True)
    link = models.URLField()

    def __str__(self):
        return self.title