from django.db import models
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    
    def __unicode__(self):
        return self.name

# Create your models here.
