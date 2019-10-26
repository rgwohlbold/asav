from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .forms import SchuelerForm
from .forms import TeilnahmeForm
from .models import Schueler
from .models import Klasse

def index(request):
    return render(request, 'verwaltung/index.html')

def erfassung(request):
    return render(request, 'verwaltung/erfassung.html')

def erfassung_schueler(request):
    if request.method == "POST":
        form = SchuelerForm(request.POST)
        if form.is_valid():
            schueler = form.save()
        return redirect('auswertung_detail', schueler_id = schueler.pk)
    else:
        form = SchuelerForm()
        return render(request, 'verwaltung/erfassung_schueler.html', {'form': form})

def erfassung_teilnahme(request):
    if request.method == "POST":
        form = TeilnahmeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('erfassung')
    else:
        form = TeilnahmeForm()
        return render(request, 'verwaltung/erfassung_schueler.html', {'form':form})

def auswertung(request):
    k = Klasse.objects.all()
    s = Schueler.objects.all()
    return render(request, 'verwaltung/auswertung.html', {'schueler': s, 'klassen': k})

def auswertung_detail(request, schueler_id):
    s = get_object_or_404(Schueler, id=schueler_id)
    teilnahmen = Schueler.objects.get(id=schueler_id).teilnahmen.select_related('aktivitaetergebnis', 'aktivitaetergebnis__ergebnis').all()
    return render(request, 'verwaltung/detail.html', {'schueler': s, 'teilnahmen': teilnahmen})

def impressum(request):
    return render(request, 'verwaltung/impressum.html')

