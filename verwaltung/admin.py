from django.contrib import admin

# Register your models here.
from .models import Schueler, Klasse, Aktivitaet, AktivitaetErgebnis, Ergebnis, Lehrer, Fach, Teilnahme

admin.site.register(Schueler)
admin.site.register(Klasse)
admin.site.register(Aktivitaet)
admin.site.register(AktivitaetErgebnis)
admin.site.register(Ergebnis)
admin.site.register(Lehrer)
admin.site.register(Fach)
admin.site.register(Teilnahme)