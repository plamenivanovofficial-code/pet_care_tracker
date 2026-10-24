from django.db import models
from pets.models import Pet
#
class CareActivity(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name