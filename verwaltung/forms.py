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
    ergebnis_name = forms.ModelChoiceField(queryset=Ergebnis.objects.all(), required=True)
    mint_punkte = forms.IntegerField(required=False)


class AktivitaetFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        ergebnisse = []
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
               continue
            ergebnis = form.cleaned_data.get('ergebnis_name')
            print(ergebnis)
            if ergebnis in ergebnisse:
                form._errors['ergebnis_name'] = ['Jedes Ergebnis darf nur einmal vorkommen!']
                raise forms.ValidationError("Jedes Ergebnis darf nur einmal vorkommen!", code='invalid')
            if ergebnis == None:
                form._errors['ergebnis_name'] = ['Sie müssen ein Ergebnis auswählen!']
                raise forms.ValidationError("Sie müssen ein Ergebnis auswählen!", code='invalid')
            ergebnisse.append(ergebnis)

