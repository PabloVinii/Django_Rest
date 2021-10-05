from django.db import models
from uuid import uuid4

# Create your models here.
class Games(models.Model):
    id_game = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    realease_date = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)