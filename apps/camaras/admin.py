from django.contrib import admin

# Register your models here.

from .models import Camara

@admin.register(Camara)
class CameraAdmin(admin.ModelAdmin):
    # Puedes personalizar la visualización de los registros de tu modelo en el panel de administración
    list_display = ('tipo', 'angulo_de_vision', 'precio', 'marca')
