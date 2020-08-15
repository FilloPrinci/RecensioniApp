from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('nuova-sezione/', views.CreaSezione.as_view(), name="crea_sezione"),
    path('sezione/<int:pk>/', views.visualizzaSezione, name="sezione_view"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)