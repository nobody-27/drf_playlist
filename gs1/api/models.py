from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    data = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return self.name