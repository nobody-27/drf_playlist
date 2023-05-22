from django.db import models

# Create your models here.

class ClassRoom(models.Model):
    name = models.CharField(max_length=100)
    class_url = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    