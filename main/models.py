from django.db import models
# Create your models here.

class Chair(models.Model):
    number = models.IntegerField("stol raqami: ")
    busy = models.BooleanField('bandmi: ', default=False)

    def __str__(self):
        return f'{self.number}'
    
class Meal(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField('price: ' , default='0.00')
    info = models.TextField('ovqat haqida: ' , default='info')
    
    def __str__(self):
        return f'{self.name} - {self.price} -- {self.info}'


class Client(models.Model):
   User_id = models.CharField(max_length=200 , default='0')
   name = models.CharField(max_length=128 , blank=True)
   meals = models.ManyToManyField(Meal, blank=True , related_name='dishes')
   chair = models.ManyToManyField(Chair , blank=True , related_name="desks")
   online = models.BooleanField('onlinemi: ', default=False)