# En views.py de tu aplicación
from django.shortcuts import render


def posicionCamaras(request):
    # Obtiene el valor de anguloVision de la URL
    anguloVision = request.GET.get('anguloVision', None)

    # Verifica si anguloVision no es None y es un número válido
    if anguloVision is not None and anguloVision.replace('.', '', 1).isdigit():
        # Convierte anguloVision a un número decimal (float)
        anguloVision = float(anguloVision)
        print(anguloVision)

    return render(request, 'posicionCamaras.html', )
