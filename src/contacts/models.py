from django.db import models
from django.utils import timezone


class Contacts(models.Model):

    listing       = models.CharField(max_length=200)
    listing_id    = models.IntegerField()
    name          = models.CharField(max_length=100)
    email         = models.CharField(max_length=100)
    phone         = models.CharField(max_length=100)
    message       = models.TextField(blank=True)
    contact_date  = models.DateTimeField(default=timezone.now)
    user_id       = models.IntegerField(blank=True)
    realtor_email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name        = 'contact'
        verbose_name_plural = 'contacts'
