# from django.shortcuts import render, redirect
# from .forms import PlanosForm
# from django.contrib import messages
# from django.conf import settings
# import os
# import cv2
# import easyocr
#
# def encontrar_numeros(imagen):
#     # Lee la imagen con OpenCV
#     img = cv2.imread(imagen)
#     if img is None:
#         raise ValueError("No se pudo cargar la imagen.")
#
#     # Convierte la imagen a escala de grises
#     gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # Aplica umbral para obtener una imagen binaria
#     _, umbral = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY_INV)
#
#     # Encuentra contornos en la imagen binaria
#     contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # Inicializa la lista de números encontrados
#     numeros_encontrados = []
#
#     # Crea el lector OCR de easyocr
#     reader = easyocr.Reader(['en'])
#
#     # Recorre todos los contornos
#     for contorno in contornos:
#         # Calcula el rectángulo que encierra el contorno
#         x, y, ancho, alto = cv2.boundingRect(contorno)
#
#         # Filtra dimensiones pequeñas que pueden ser ruido
#         if ancho > 10 and alto > 10:
#             # Recorta la región de interés (ROI) de la imagen original
#             roi = img[y:y+alto, x:x+ancho]
#
#             # Convierte la ROI a escala de grises
#             roi_gris = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#
#             # Utiliza easyocr para realizar el reconocimiento de texto
#             resultados = reader.readtext(roi_gris)
#
#             # Extrae el texto de los resultados y agrega a la lista
#             for resultado in resultados:
#                 numeros_encontrados.append(resultado[1])
#
#     return numeros_encontrados
#
# def disenoPlanos(request):
#     if request.method == 'POST':
#         form = PlanosForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Guarda la imagen
#             form.save()
#
#             # Obtiene la última imagen guardada en media/planos
#             lista_imagenes = os.listdir(os.path.join(settings.MEDIA_ROOT, 'planos'))
#             if lista_imagenes:
#                 ultima_imagen = lista_imagenes[-1]
#                 imagen_path = os.path.join(settings.MEDIA_ROOT, 'planos', ultima_imagen)
#
#                 try:
#                     # Verifica si es un plano y obtiene los números
#                     numeros_encontrados = encontrar_numeros(imagen_path)
#
#                     # Aquí puedes realizar cualquier acción adicional con los números obtenidos
#
#                     # Ejemplo de cómo imprimir los números en la consola del servidor
#                     print("Números encontrados:", numeros_encontrados)
#
#                 except ValueError as error:
#                     # Si no se encuentran números, genera un mensaje de error
#                     messages.error(request, f'Error al procesar la imagen: {error}')
#             else:
#                 messages.error(request, 'No hay imágenes de planos para procesar.')
#         else:
#             messages.error(request, 'Hubo un error al cargar el plano. Verifica los datos ingresados.')
#     else:
#         form = PlanosForm()
#     return render(request, 'disenoPlanos.html', {'form': form})
