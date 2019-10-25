from django import forms
from .models import Schueler

class SchuelerForm(forms.ModelForm):

    class Meta:
        model = Schueler
        fields= ('vname', 'nname', 'klasse', 'email')
