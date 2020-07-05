from django.urls import path
from . import views

urlpatterns = [
    path('nuova-sezione/', views.CreaSezione.as_view(), name="crea_sezione"),
    path('sezione/<int:pk>/', views.visualizzaSezione, name="sezione_view"),
    path('sezione/<int:pk>/rispondi/', views.aggiungiRisposta, name="risposta_seizone")
]