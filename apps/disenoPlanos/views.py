from django.shortcuts import render, redirect
from .forms import PlanosForm
from django.contrib import messages
import cv2
import pytesseract
from django.urls import reverse


def disenoPlanos(request):
    anguloVision = request.GET.get('anguloVision', None)

    if request.method == 'POST':
        form = PlanosForm(request.POST, request.FILES)
        if form.is_valid():
            plano = form.save(commit=False)
            plano.save()

            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

            # Cargamos la imagen original
            original = cv2.imread(plano.imagen.path)

            # Preprocesamiento
            gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (5, 5), 0)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

            # Encuentra contornos en la imagen binarizada
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Reconoce números y comas
            texto_numeros_comas = pytesseract.image_to_string(original,
                                                              config='--psm 6 -c tessedit_char_whitelist=0123456789,')
            texto_numeros_comas = texto_numeros_comas.replace(',', '.')

            # Almacena los textos reconocidos en una lista
            textos_reconocidos = [texto_numeros_comas]

            # Almacena los textos reconocidos en una tupla
            medidas = tuple(texto_numeros_comas.split())

            print(medidas)

            # Utiliza reverse para obtener la URL con los argumentos de palabra clave
            url = reverse('camaras')

            # Agrega los argumentos de palabra clave a la URL
            url += f'?anguloVision={anguloVision}&medidas={",".join(map(str, medidas))}'

            return redirect(url)

        else:
            messages.error(request, 'Hubo un error al cargar el plano. Verifica los datos ingresados.')

    else:
        form = PlanosForm()
    return render(request, 'disenoPlanos.html', {'form': form, 'anguloVision': anguloVision})
