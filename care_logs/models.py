from django.db import models
from pets.models import Pet

class CareActivity(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField(blank=True)
    pet = models.ForeignKey(
        Pet, 
        on_delete=models.CASCADE,
        related_name='care_activities',
    )
    
    class Meta:
        ordering = ['-date']
 
    def __str__(self):
        return f'{self.name} - {self.pet}'