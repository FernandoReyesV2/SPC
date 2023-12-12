from django.shortcuts import render, redirect
from .forms import PlanosForm
from django.contrib import messages
import cv2
import pytesseract
import os
from django.conf import settings


def disenoPlanos(request):
    if request.method == 'POST':
        form = PlanosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Configura la ruta al ejecutable de Tesseract OCR
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ajusta la ruta según tu instalación

            # Cargamos la imagen
            original = cv2.imread("E:\habitaicon.jpg")
            # cv2.imshow("original", original)
            cv2.waitKey(0)

            # Reconoce números y comas
            texto_numeros_comas = pytesseract.image_to_string(original,
                                                              config='--psm 6 -c tessedit_char_whitelist=0123456789,')
            texto_numeros_comas = texto_numeros_comas.replace(',', '.')  # Si es necesario reemplazar comas por puntos

            # Almacena los textos reconocidos en una lista
            textos_reconocidos = [texto_numeros_comas]

            # Almacena los textos reconocidos en una tupla
            medidas = tuple(texto_numeros_comas.split())  # Convierte el texto en una tupla

            print(medidas)
            return redirect('posicionCamaras')

        else:
            messages.error(request, 'Hubo un error al cargar el plano. Verifica los datos ingresados.')

    else:
        form = PlanosForm()
    return render(request, 'disenoPlanos.html', {'form': form})
