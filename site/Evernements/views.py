from django.shortcuts import render
from .models import Evenement
from datetime import date
from django.utils import timezone

def projet(request):
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

    return render(request, 'Evernements/projet.html', {'evenements': evenements})




def evenement_detail(request, evenement_id):
    evenement = Evenement.objects.get(id=evenement_id)
    return render(request, 'Evernements/show.html', {'evenement': evenement})

