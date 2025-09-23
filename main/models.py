import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('t-shirt', 'T-shirt'),
        ('jacket', 'Jacket'),
        ('shoes', 'Shoes'),
        ('socks', 'Socks'),
        ('ball', 'Ball'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)