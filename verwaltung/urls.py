from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('erfassung', views.erfassung, name='erfassung'),
    path('auswertung', views.auswertung, name='auswertung'),
    path('auswertung/<int:schueler_id>', views.auswertung_detail, name='auswertung_detail'),
    path('impressum', views.impressum, name='impressum'),
]