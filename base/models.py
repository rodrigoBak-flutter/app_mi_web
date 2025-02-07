from django.db import models

class Client(models.Model):
    name= models.CharField(max_length=30)
    address= models.CharField(max_length=50)
    email=models.EmailField() #si quiero cambiar el nombre de como se va a ver en el panel de administracion verbose_name= "Correo"
    phone=models.CharField( max_length=9) #Si quiero que no sae un campo requerido hago blank=True,, null=True
    
    def __str__(self):
        return 'Cliente: %s, Direccion: %s, Correo %s, y Telefono: %s' %(self.name,self.address ,self.email,self.phone)
    
class Articles(models.Model):
    name=models.CharField(max_length=30)
    section=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    
    #Con esto me devuelve raqueta, la seccion, el nombre, precio
    def __str__(self):
        return 'Nombre: %s, Seccion: %s y Precio: %s' %(self.name, self.section,self.price)
    

class Orders(models.Model):
    number= models.IntegerField()
    date= models.DateField()
    delivered=models.BooleanField()
    
    def __str__(self):
        return 'Numero pedido: %s, Fecha: %s y Enviado: %s' %(self.number, self.date,self.delivered)
    