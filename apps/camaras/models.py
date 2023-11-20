from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
from io import BytesIO

# Create your models here.
class Camara(models.Model):
    # Opciones para el atributo tipo
    TIPO_CHOICES = [
        ('interior', 'Interior'),
        ('exterior', 'Exterior'),
    ]

    # Atributo para el tipo de cámara, con opciones predefinidas "interior" y "exterior"
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    # Atributo para el nombre de la cámara
    nombre = models.CharField(max_length=100, default="SinNombre")

    # Atributo para el ángulo de visión, puedes usar un campo Decimal o FloatField para almacenar valores numéricos.
    angulo_de_vision = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(360)])

    # Atributo para el precio, puedes usar un campo Decimal o FloatField para almacenar valores numéricos.
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    # Atributo para la marca de la cámara.
    marca = models.CharField(max_length=100)

    # Atributo para la resolución de la cámara (acepta valores numéricos enteros)
    resolucion = models.IntegerField(default=720)  # Establece 720 como valor predeterminado

    # Atributo para la rotación de la cámara (acepta valores numéricos enteros)
    rotacion = models.IntegerField(default=0) # Puedes ajustar este campo según tus necesidades, por ejemplo, usar FloatField si necesitas decimales

    # Atributo para guardar una imagen convertida a una secuencia de bytes
    imagen = models.ImageField(upload_to='camaras/', blank=True, null=True)

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.marca}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.imagen:
            # Abre la imagen con Pillow y conviértela a una secuencia de bytes
            img = Image.open(self.imagen.path)
            buffer = BytesIO()
            img.save(buffer, format='JPEG')
            byte_sequence = buffer.getvalue()
            # Actualiza el campo imagen_bytes con la secuencia de bytes
            self.imagen_bytes = byte_sequence
            super().save(*args, **kwargs)