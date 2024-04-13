from django.db import models
from django.utils import timezone

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} - {'Disponible' if self.disponible else 'No disponible'} - Capacidad: {self.capacidad}" 

class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre_de_usuario} - {self.clase.nombre} - {self.fecha}"