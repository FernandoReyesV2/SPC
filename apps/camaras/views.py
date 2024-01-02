from django.shortcuts import render
from .models import Camara, Sensores

def camaras(request):
    # Obtén el valor de medidas
    medidas_str = request.GET.get('medidas', None)

    if medidas_str:
        medidas = tuple(map(float, medidas_str.split(',')))

    # Obtener todas las cámaras desde la base de datos
    camaras = Camara.objects.all()

    # Obtener categorías únicas de la base de datos
    categorias_tipo = Camara.objects.values_list('tipo', flat=True).distinct()
    categorias_precio = Camara.objects.values_list('precio', flat=True).distinct()
    categorias_marca = Camara.objects.values_list('marca', flat=True).distinct()
    categorias_resolucion = Camara.objects.values_list('resolucion', flat=True).distinct()
    categorias_angulo_de_vision = Camara.objects.values_list('angulo_de_vision', flat=True).distinct()
    categorias_nombre = Camara.objects.values_list('nombre', flat=True).distinct()

    # Obtener el límite de cámaras según el área de la habitación
    limite_cameras = areaHabitacion(medidas)

    # Renderizar la página con la lista de cámaras y categorías
    return render(request, 'camaras.html', {
        'camaras': camaras,
        'categorias_tipo': categorias_tipo,
        'categorias_precio': categorias_precio,
        'categorias_marca': categorias_marca,
        'categorias_resolucion': categorias_resolucion,
        'angulo_de_vision': categorias_angulo_de_vision,
        'nombre': categorias_nombre,
        'limite_cameras': limite_cameras,
        'medidas': medidas,
    })


def areaHabitacion(medidas):
    area = medidas[0] * medidas[1]
    limite_cameras = 2 if area <= 20 else 4
    print("area",area)
    return limite_cameras
