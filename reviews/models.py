from django.db import models

# Create your models here.
class Review(models.Model):
    review_text = models.CharField(max_length=100, blank=True)
    person = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)