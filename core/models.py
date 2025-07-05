from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    sup=models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else f"Contact {self.id}"