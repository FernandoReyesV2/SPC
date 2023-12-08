from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.validators import MinValueValidator, MaxValueValidator

class Usuario(models.Model):

    angulo_de_vision = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(360)])

class CambiarPlanos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()



class CambiarHardware(models.Model):
    nombre = models.CharField(max_length=255)
    especificaciones = models.TextField()


class ExportarPDF(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='pdfs/')
