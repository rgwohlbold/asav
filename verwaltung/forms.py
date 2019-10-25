from django import forms
from .models import Schueler, Teilnahme

class SchuelerForm(forms.ModelForm):

    class Meta:
        model = Schueler
        fields= ('vname', 'nname', 'klasse', 'email')


class TeilnahmeForm(forms.ModelForm):

    class Meta:
        model = Teilnahme
        fields = ('schueler', 'aktivitaetergebnis', 'lehrer1', 'lehrer2', 'schuljahr')
