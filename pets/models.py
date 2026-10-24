from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    category = models.CharField(max_length=30, blank=False, null=False)
    age = models.CharField(blank=False, null=False)
    peronal_photo = models.URLField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name 