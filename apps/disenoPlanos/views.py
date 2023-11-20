from django.shortcuts import render

# Create your views here.
def disenoPlanos(request):
    return render(request, 'disenoPlanos.html')