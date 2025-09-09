from django.db import models

class Store(models.Model):
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20)
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
