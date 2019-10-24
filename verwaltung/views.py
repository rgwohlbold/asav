from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Schueler, AktivitaetErgebnis, Teilnahme

# Create your views here.
def index(request):
    s = Schueler.objects.all()
    return render(request, 'verwaltung/index.html', {'schueler': s})

def detail(request, schueler_id):
    s = get_object_or_404(Schueler, id=schueler_id)
    teilnahmen = Schueler.objects.get(id=schueler_id).teilnahmen.select_related('aktivitaetergebnis', 'aktivitaetergebnis__ergebnis').all()
    return render(request, 'verwaltung/detail.html', {'schueler': s, 'teilnahmen': teilnahmen})

