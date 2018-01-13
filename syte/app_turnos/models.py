from django.db import models

# Create your models here.
class Institucion(models.Model):
	nombre = models.CharField(max_length = 50)
	detalle = models.CharField(max_length = 120,null=True,default="")

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']

class Visitante(models.Model):
	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50)
	dni = models.IntegerField()
	telefono = models.IntegerField()	
	institucion = models.ForeignKey(Institucion, related_name="visitante")
	
	def __str__(self):
		return self.nombre

class Turno(models.Model):
	TIPO = (("exclusivo","limitado"),)
	fecha = models.DateField()
#	horario = models.datetime()
	visitante = models.ForeignKey(Visitante, related_name="turno")
	tipo = models.CharField(max_length = 10, choices = TIPO)	
	habilitada = models.BooleanField(default=True)