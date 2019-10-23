from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Schueler, AktivitaetErgebnis

# Create your views here.
def index(request):
    s = Schueler.objects.all()
    return render(request, 'verwaltung/index.html', {'schueler': s})

def detail(request, schueler_id):
    s = get_object_or_404(Schueler, id=schueler_id)
    for i in AktivitaetErgebnis.objects.raw('SELECT verwaltung_aktivitaetergebnis.mint_punkte FROM verwaltung_teilnahme WHERE schueler_id=2 INNER JOIN verwaltung_aktivitaetergebnis ON verwaltung_teilnahme.aktivitaet_id=verwaltung_aktivitaetergebnis.aktivitaet_id'):
        print(i)
    return render(request, 'verwaltung/detail.html', {'schueler': s})


