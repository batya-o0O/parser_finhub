from django.db import models

# Create your models here.
class Quote(models.Model):
    name = models.CharField(max_length=5)
    current = models.FloatField()
    change = models.FloatField()
    percent_change = models.FloatField()
    hayday = models.FloatField() 
    lowday = models.FloatField()
    openday= models.FloatField()
    prevclose = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return self.name