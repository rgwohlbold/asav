from django.urls import path

from . import views

urlpatterns = [
    path('schueler', views.index, name='index'),
    path('schueler/<int:schueler_id>', views.detail, name='schueler_detail')
]