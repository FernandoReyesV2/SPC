from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from .utils import calcular_posiciones_optimas  # Importa la función de cálculo desde un módulo utilitario

def posicionCamaras(request):
    medidas_habitacion = (10, 8, 12)
    medidas_camara = (2, 2)
    angulo_vision = 90
    areas_interes = [(2, 3), (5, 7), (8, 2)]

    # Calcula las posiciones óptimas de las cámaras
    posiciones_optimas = calcular_posiciones_optimas(medidas_habitacion, medidas_camara, angulo_vision, areas_interes)

    # Pasa los resultados al contexto de la plantilla
    context = {
        'posiciones_optimas': posiciones_optimas,
    }

    return render(request, 'posicionCamaras.html')
