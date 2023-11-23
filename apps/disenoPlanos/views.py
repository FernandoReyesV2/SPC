from django.shortcuts import render, redirect
from .forms import PlanosForm

def disenoPlanos(request):
    if request.method == 'POST':
        form = PlanosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PlanosForm()
    return render(request, 'disenoPlanos.html', {'form': form})
