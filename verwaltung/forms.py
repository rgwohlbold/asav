from django import forms
from .models import Schueler, Teilnahme, Fach, Ergebnis
from django.forms.formsets import BaseFormSet


class SchuelerForm(forms.ModelForm):

    class Meta:
        model = Schueler
        fields= ('vname', 'nname', 'klasse', 'email')


class TeilnahmeForm(forms.ModelForm):

    class Meta:
        model = Teilnahme
        fields = ('schueler', 'aktivitaetergebnis', 'lehrer1', 'lehrer2', 'schuljahr')


class BaseAktivitaetForm(forms.Form):
    aktivitaet_name = forms.CharField(max_length=100)
    fach = forms.ModelChoiceField(queryset=Fach.objects.all())

class AktivitaetForm(forms.Form):
    ergebnis_name = forms.ModelChoiceField(queryset=Ergebnis.objects.all())
    mint_punkte = forms.IntegerField()


class AktivitaetFormSet(BaseFormSet):
    pass


