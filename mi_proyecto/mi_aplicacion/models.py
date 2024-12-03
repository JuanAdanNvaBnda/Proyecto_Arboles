from django.db import models

# Create your models here.


class Grado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Arbol(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    edad_aproximada = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes_arboles/')

    #AGREGAR CAMPOS DESCRIPCION, CUIDADOS Y RIEGOS POR SEMANA || TEXT, TEXT, INT

    descripcion = models.TextField(null=True, blank=True)
    cuidados = models.TextField(null=True, blank=True)
    riego_por_semana = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre



