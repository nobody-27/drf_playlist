from django.db import models

# Create your models here.

class Token_Testing(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=243)
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super(self.name).__str__()
    