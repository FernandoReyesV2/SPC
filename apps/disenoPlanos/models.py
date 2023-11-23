from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
class Planos(models.Model):

    # Atributo para guardar una imagen convertida a una secuencia de bytes
    imagen = models.ImageField(upload_to='planos/', blank=True, null=True)

    def __str__(self):
        return f'Imagen de plano: {self.imagen.name}' if self.imagen else 'Plano sin imagen'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.imagen:
            # Llama a la función utilitaria para convertir la imagen a bytes
            byte_sequence = convertir_imagen_a_bytes(self.imagen.path)
            if byte_sequence:
                # Actualiza el campo imagen con la secuencia de bytes
                self.imagen.save('imagen.jpg', ContentFile(byte_sequence), save=False)
                super().save(*args, **kwargs)

def convertir_imagen_a_bytes(imagen_path):
    try:
        with Image.open(imagen_path) as img:
            buffer = BytesIO()
            img.save(buffer, format='JPEG')
            byte_sequence = buffer.getvalue()
            return byte_sequence
    except Exception as e:
        raise ValueError(f"Error al convertir la imagen a bytes: {e}")