# En views.py de tu aplicación
from django.shortcuts import render
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
from django.conf import settings
from datetime import datetime

def posicionCamaras(request):
    anguloVision = []
    # Obtiene el valor de anguloVision de la URL
    angulo_Vision = request.GET.get('anguloVision', None)
    medidas_str = request.GET.get('medidas', None)

    # Verifica si anguloVision no es None y es una lista de números válidos
    if angulo_Vision is not None:
        # Convierte los ángulos de string a una lista de flotantes
        angulo_Vision = [float(angulo) for angulo in angulo_Vision.split(',') if angulo.replace('.', '', 1).isdigit()]

        # Asegúrate de que la lista de ángulos no tenga más de 4 elementos
        angulo_Vision = angulo_Vision[:4]

        # Agrega todos los ángulos a la lista
        anguloVision.extend(angulo_Vision)
        print("Ángulos:", anguloVision)

    if medidas_str:
        medidas = tuple(map(float, medidas_str.replace('(', '').replace(')', '').split(',')))

    # Vertice inicial
    vertice = (0, 0)

    # Puntos para graficar la habitacion
    vertices_cuadrilatero = [(0, 0), (0, medidas[1]), (medidas[0], medidas[1]), (medidas[0], 0)]

    # Colors for each sector
    sector_colors = ['red', 'green', 'blue', 'orange']

    contador = 0

    # Genera un nombre de archivo único con la marca de tiempo
    timestamp_str = datetime.now().strftime("%Y%m%d%H%M%S")
    image_filename = f"posicionCamaras_{timestamp_str}.png"

    # Ruta donde se guardará la imagen del gráfico
    image_path = os.path.join(settings.MEDIA_ROOT, 'grafico', image_filename)

    # Asegúrate de que la carpeta de destino exista
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    # Pasa la ruta de la imagen como contexto a la función render
    context = {'image_path': os.path.join(settings.MEDIA_URL, 'grafico', image_filename)}

    # Configuracion del Grafico
    x, y = zip(*vertices_cuadrilatero)
    plt.plot(x + (x[0],), y + (y[0],), 'k-')
    plt.fill(x, y, alpha=0.2, color='gray')

    plt.title('Posicion Optima Cámara')
    plt.axis('equal')

    for angulo, color in zip(anguloVision, sector_colors):
        contador += 1
        if contador == 1:
            if angulo > 90:
                vertice = (medidas[0] / 2, 0)
            else:
                vertice = (0, 0)
        elif contador == 2:
            if angulo > 90:
                vertice = (0, medidas[1] / 2)
            else:
                vertice = (0, medidas[1])
        elif contador == 3:
            if angulo > 90:
                vertice = (medidas[0] / 2, medidas[1])
            else:
                vertice = (medidas[0], medidas[1])
        elif contador == 4:
            if angulo > 90:
                vertice = (medidas[0], medidas[1] / 2)
            else:
                vertice = (medidas[0], 0)
        Calcular(vertice, angulo, contador, color, medidas)

    # Guardar la figura en un archivo
    plt.savefig(image_path)

    plt.close()

    return render(request, 'posicionCamaras.html', context)

# Calcular el ángulo entre dos puntos con respecto al eje x positivo
def calcular_angulo_entre_puntos(angulo, contador):
    # sector 1
    if contador == 1:
        if angulo < 90:
            angulo_deg = 45 - angulo / 2
        elif angulo == 90:
            angulo_deg = 0
        else:
            angulo_deg = 90 - angulo / 2
    # sector 2
    elif contador == 2:
        if angulo < 90:
            angulo_deg = (315 - angulo / 2)
        elif angulo == 90:
            angulo_deg = 270
        else:
            angulo_deg = (360 - angulo / 2)
    # sector 3
    elif contador == 3:
        if angulo < 90:
            angulo_deg = (225 - angulo / 2)
        elif angulo == 90:
            angulo_deg = 180
        else:
            angulo_deg = (270 - angulo / 2)
    # sector 4
    elif contador == 4:
        if angulo < 90:
            angulo_deg = (135 - angulo / 2)
        elif angulo == 90:
            angulo_deg = 90
        else:
            angulo_deg = (180 - angulo / 2)
    else:
        angulo_deg = 0

    return angulo_deg

# Grafica el rango de visión como un sector circular y el cuadrilátero
def Calcular(vertice, angulo, contador, color, medidas):
    angulo_inicial = calcular_angulo_entre_puntos(angulo, contador)
    sector_radius = medidas[0] / 2
    sector = patches.Wedge(vertice, sector_radius, angulo_inicial, angulo_inicial + angulo, alpha=0.2, color=color)
    plt.gca().add_patch(sector)

    # Posicion de las camaras
    plt.scatter(vertice[0], vertice[1], color='black', marker='o')