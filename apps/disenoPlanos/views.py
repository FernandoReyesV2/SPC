from django.shortcuts import render, redirect
from .forms import PlanosForm
from django.contrib import messages

def disenoPlanos(request):
    if request.method == 'POST':
        form = PlanosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posicionCamaras')
        else:
            messages.error(request, 'Hubo un error al cargar el plano. Verifica los datos ingresados.')
    else:
        form = PlanosForm()
    return render(request, 'disenoPlanos.html', {'form': form})
