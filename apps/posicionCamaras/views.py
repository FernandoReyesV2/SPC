# En views.py de tu aplicación
from django.shortcuts import render
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
from django.conf import settings
from datetime import datetime

def posicionCamaras(request):
    # Obtiene el valor de anguloVision de la URL
    anguloVision = request.GET.get('anguloVision', None)

    # Verifica si anguloVision no es None y es un número válido
    if anguloVision is not None and anguloVision.replace('.', '', 1).isdigit():
        # Convierte anguloVision a un número decimal (float)
        anguloVision = float(anguloVision)
        print(anguloVision)

    # Punto inicial del sector circular
    vertice = (0, 0)

    if anguloVision > 90:
        vertice = (1.5, 0)

    # Genera un nombre de archivo único con la marca de tiempo
    timestamp_str = datetime.now().strftime("%Y%m%d%H%M%S")
    image_filename = f"posicionCamaras_{timestamp_str}.png"

    # Ruta donde se guardará la imagen del gráfico
    image_path = os.path.join(settings.MEDIA_ROOT, 'grafico', image_filename)

    # Asegúrate de que la carpeta de destino exista
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    Calcular(vertice, anguloVision, image_path)

    # Pasa la ruta de la imagen como contexto a la función render
    context = {'image_path': os.path.join(settings.MEDIA_URL, 'grafico', image_filename)}

    return render(request, 'posicionCamaras.html', context)

def calcular_angulo_entre_puntos(anguloVision):
    if anguloVision < 90:
        angulo_deg = 45 - anguloVision / 2
    elif anguloVision == 90:
        angulo_deg = 0
    else:
        angulo_deg = 90 - anguloVision / 2
    return angulo_deg

def Calcular(vertice, angulo, image_path):
    # Calcular el ángulo entre el eje x positivo y el vector formado por vertice
    angulo_inicial = calcular_angulo_entre_puntos(angulo)

    # Graficar el sector circular
    sector = patches.Wedge(vertice, max(medidas), angulo_inicial, angulo_inicial + angulo, alpha=0.5, color='red')
    plt.gca().add_patch(sector)

    # Descomprimir las coordenadas x e y del cuadrilátero
    x, y = zip(*vertices_cuadrilatero)

    # Graficar el cuadrilátero
    plt.plot(x, y, marker='')
    plt.fill(x, y, alpha=0.2)

    # Configuraciones adicionales del gráfico
    # plt.title('Sector Circular y Cuadrilátero')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.grid(False)
    plt.axis('equal')  # Hacer que los ejes tengan la misma escala

    # Guardar la figura en un archivo
    plt.savefig(image_path)

    plt.close()

# Medidas para la habitación
medidas = (3, 3)

# Coordenadas del cuadrilátero
vertices_cuadrilatero = [(0, 0), (0, medidas[1]), (medidas[0], medidas[1]), (medidas[0], 0)]

