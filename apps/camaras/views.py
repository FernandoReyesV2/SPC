from django.shortcuts import render

# Create your views here.
def camaras(request):
    return render(request, 'camaras.html')
