from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auswertung', views.auswertung, name='auswertung'),
    path('schueler', views.liste, name='schueler_liste'),
    path('schueler/<int:schueler_id>', views.detail, name='schueler_detail'),
    path('impressum', views.impressum, name='impressum'),
]