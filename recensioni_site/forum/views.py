from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Sezione, PostModelForm
from .mixins import StaffMixing

# Create your views here.
class CreaSezione(StaffMixing, CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url = "/"

def visualizzaSezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    form_risposta = PostModelForm()
    context = {"sezione": sezione, "form_risposta" : form_risposta}
    return render(request, "forum/singola_sezione.html", context )

def aggiungiRisposta(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    if(request.method=='POST'):
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.sezione = sezione
            form.instance.autore_post = request.user
            form.instance.discussione = sezione
            form.save()
            url_sezione = reverse("sezione_view", kwargs={"pk": pk})
            return HttpResponseRedirect(url_sezione)
        else:
            return HttpResponseBadRequest();

