from django.db import models

# Create your models here.
'''
 ORM : OBJECT RELATIONAL MAPPING 
 makemigrations 
 migrate
'''

class airport(models.Model):
    code=models.CharField(max_length=55)
    city=models.CharField(max_length=55)

    def __str__(self):
        return f"Airport ({self.city}({self.code}))"

class flight(models.Model):
    origin=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='departure')
    destinations=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='arrival')
    durations=models.IntegerField()

    def __str__(self):
        return f"{self.origin} - {self.destinations}"

class passenger(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    flights=models.ManyToManyField(flight,related_name="passengers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
