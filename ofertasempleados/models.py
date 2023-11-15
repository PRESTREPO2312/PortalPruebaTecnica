
from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    nit = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre + ' ' +self.nit

class Oferta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    habilidades = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion_perfil = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)

class Postulacion(models.Model):
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
