from django.db import models

# Create your models here.
'''
 ORM : OBJECT RELATIONAL MAPPING 
 makemigrations 
 migrate
'''
class flight(models.Model):
    origin=models.CharField(max_length=35)
    destinations=models.CharField(max_length=35)
    durations=models.IntegerField()

    def __str__(self):
        return f"{self.origin} - {self.destinations}"