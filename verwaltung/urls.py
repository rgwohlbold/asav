from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('erfassung', views.erfassung, name='erfassung'),
    path('auswertung', views.auswertung, name='auswertung'),
    path('auswertung/<int:schueler_id>', views.auswertung_detail, name='auswertung_detail'),
    path('impressum', views.impressum, name='impressum'),
    path('erfassung/schueler', views.erfassung_schueler, name='erfassung_schueler'),
    path('erfassung/teilnahme', views.erfassung_teilnahme, name='erfassung_teilnahme'),
    path('erfassung/aktivitaet', views.erfassung_aktivitaet, name='erfassung_aktivitaet')
]