from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.forms.formsets import formset_factory
from django.db.models import Q

from .forms import SchuelerForm
from .forms import TeilnahmeForm
from .forms import AktivitaetForm
from .forms import BaseAktivitaetForm
from .forms import AktivitaetFormSet
from .models import Schueler
from .models import Klasse
from .models import Aktivitaet
from .models import AktivitaetErgebnis
from .models import Ergebnis

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
    return render(request, 'verwaltung/erfassung_teilnahme.html', {'form':form})


def erfassung_aktivitaet(request):
    formset = formset_factory(AktivitaetForm, AktivitaetFormSet)
    if request.method== "POST":
        form = BaseAktivitaetForm(request.POST)
        bound_formset = formset(request.POST)
        print(form.is_valid())
        print(bound_formset.is_valid())
        print(bound_formset.errors)
        if form.is_valid() and bound_formset.is_valid():
            akt = Aktivitaet()
            akt.name = form.cleaned_data.get('aktivitaet_name')
            akt.fach = form.cleaned_data.get('fach')
            akt.save()

            for bound_form in bound_formset:
                akt_erg = AktivitaetErgebnis()
                akt_erg.aktivitaet = akt
                akt_erg.mint_punkte = bound_form.cleaned_data.get('mint_punkte')
                akt_erg.ergebnis = bound_form.cleaned_data.get('ergebnis_name')
                akt_erg.save()
            return redirect('erfassung')
    else:
        bound_formset = formset
        form = BaseAktivitaetForm()
    return render(request, 'verwaltung/erfassung_aktivitaet.html', {'form': form, 'formset': bound_formset})




def auswertung(request):
    s = Schueler.objects.all()
    if request.method == 'GET':
        query = request.GET.get('q')
        if query != None and query != "":
            s = Schueler.objects.filter(Q(vname__icontains=query) | Q(nname__icontains=query))
            
            klassen = []
            for schueler in s:
                klassen.append(schueler.klasse)
            u_klassen = set(klassen)
            klassen = list(u_klassen)
            return render(request, 'verwaltung/suchergebnisse.html', {'schueler': s, 'klassen': klassen})
    klassen = []
    for schueler in s:
        klassen.append(schueler.klasse)
    u_klassen = set(klassen)
    klassen = list(u_klassen)
    return render(request, 'verwaltung/auswertung.html', {'schueler': s, 'klassen': klassen})


def auswertung_detail(request, schueler_id):
    s = get_object_or_404(Schueler, id=schueler_id)
    teilnahmen = Schueler.objects.get(id=schueler_id).teilnahmen.select_related('aktivitaetergebnis', 'aktivitaetergebnis__ergebnis').all()
    return render(request, 'verwaltung/detail.html', {'schueler': s, 'teilnahmen': teilnahmen})

def impressum(request):
    return render(request, 'verwaltung/impressum.html')

