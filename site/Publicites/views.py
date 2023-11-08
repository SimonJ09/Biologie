from django.shortcuts import render
from .models import Publicite
from Evernements.models import Evenement
from django.shortcuts import render
from datetime import date
from django.utils import timezone

def accueil(request):
    publicites = Publicite.objects.all()
    evenements = Evenement.objects.all()
    filter_type = request.GET.get('filter_type','all')
    print(filter_type)
    today = timezone.now().date()
    if filter_type == 'en_cours':
        evenements = evenements.filter(date_debut__lte=today, date_fin__gte=today)
    elif filter_type == 'terminees':
        evenements = evenements.filter(date_fin__lt=today)
    elif filter_type == 'avenir':
        evenements = evenements.filter(date_debut__gt=today)
    elif filter_type == 'participer':
        evenements = evenements.filter(date_fin__gt=today)  # Modifiez cela en fonction de vos critères.

    return render(request, 'Publicites/index.html', {'publicites': publicites,'evenements': evenements })



   