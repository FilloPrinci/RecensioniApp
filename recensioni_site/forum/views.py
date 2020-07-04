from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Sezione

# Create your views here.
class CreaSezione(CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"

