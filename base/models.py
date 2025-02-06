from django.db import models

class Client(models.Model):
    name= models.CharField(max_length=30)
    address= models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField( max_length=9)
    
    
class Articles(models.Model):
    name=models.CharField(max_length=30)
    section=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    

class Orders(models.Model):
    number= models.IntegerField()
    fecha= models.DateField()
    delivered=models.BooleanField()
    