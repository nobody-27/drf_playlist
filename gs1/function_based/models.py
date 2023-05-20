from django.db import models

# Create your models here.

class NoteBook(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    