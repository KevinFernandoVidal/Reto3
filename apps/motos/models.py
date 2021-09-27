from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    foto  = models.ImageField(upload_to='fotos_usuarios', null=True, blank=True)
    cedula = models.IntegerField(unique=True)
    telefono = models.IntegerField(null=True, blank=True)
    dirección = models. CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def nombreCompleto(self):
        txt = "{0}, {1}"
        return txt.format(self.nombres, self.apellidos)

    def __str__(self):
        return self.nombres + " " + self.apellidos
    
class Moto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cilindraje = models.IntegerField()
    foto_moto = models.ImageField(upload_to='fotos_motos', null=True, blank=True)
    color = models.CharField(max_length=100)
    placa = models.CharField(unique=True, max_length=100) 
    chasis = models.CharField(unique=True, max_length=100)

    def nombreCompleto(self):
        txt = "{0}, {1}"
        return txt.format(self.marca, self.modelo)
    
    def __str__(self):
        return self.marca + " " + self.modelo
estados=(
    ('Vendida', 'Vendida'),
    ('Rechazada', 'Rechazada'),
    ('Pendiente old', 'Pendiente'),
    ('Pendiente new', 'Pendiente'),
    ('En propiedad', 'En propiedad'),

)

class Historial(models.Model):
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Persona, on_delete=models.PROTECT)
    estado = models.CharField(max_length=20, choices= estados, default='En propiedad') 

    def __str__(self):
        return str(self.moto) + " " + self.estado 


class  Mantenimientos(models.Model):
    nombres     = models.CharField(max_length=100)
    fecha       = models.DateTimeField(auto_now=True)
    descripción = models.TextField(null=True, blank=True)
    responsable = models.ForeignKey(Persona, on_delete=models.PROTECT)
    moto        = models.ForeignKey(Moto, on_delete=models.CASCADE)
