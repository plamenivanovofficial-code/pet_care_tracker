from django.db import models

class Tag(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
    )
    
    def __str__(self):
        return self.name
    
    
class Pet(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    main_photo = models.URLField()
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='pets',
    )
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name 