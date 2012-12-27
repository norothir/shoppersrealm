from django.db import models

# Create your models here.
class Ostos(models.Model):
    
    item = models.CharField(max_length=45)
    amount = models.DecimalField(max_digits=12,decimal_places=2)
    category = models.CharField(max_length=45)
    buyer = models.CharField(max_length=45)
    active = models.IntegerField()
    listid = models.IntegerField()
    
    
    def __unicode__(self):
        return "%s %d" %(self.item,self.amount)
    
    
    