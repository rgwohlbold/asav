from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Schueler

def index(request):
    return render(request, 'verwaltung/index.html')

def erfassung(request):
    return render(request, 'verwaltung/erfassung.html')

def auswertung(request):
    s = Schueler.objects.all()
    return render(request, 'verwaltung/auswertung.html', {'schueler': s})

def auswertung_detail(request, schueler_id):
    s = get_object_or_404(Schueler, id=schueler_id)
    teilnahmen = Schueler.objects.get(id=schueler_id).teilnahmen.select_related('aktivitaetergebnis', 'aktivitaetergebnis__ergebnis').all()
    return render(request, 'verwaltung/detail.html', {'schueler': s, 'teilnahmen': teilnahmen})

def impressum(request):
    return render(request, 'verwaltung/impressum.html')

