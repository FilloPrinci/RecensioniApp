from django.urls import path
from .views import resgistrazioneView

urlpatterns =[
    path('registrazione/', resgistrazioneView, name='registration_view')
]