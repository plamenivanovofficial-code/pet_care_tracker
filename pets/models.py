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
    photo_url = models.URLField(blank=True)
    photo_file = models.ImageField(upload_to='pets/', blank=True)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='pets',
    )
    
    class Meta:
        ordering = ['name']

    @property
    def photo(self):
        if self.photo_file:
            return self.photo_file.url
        return self.photo_url

    def __str__(self):
        return self.name 