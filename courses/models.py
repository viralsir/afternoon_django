from django.db import models
from django.urls import  reverse

# Create your models here.
class course(models.Model):
    name=models.CharField(max_length=35)
    description=models.TextField()
    fees=models.IntegerField()

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('course-view')