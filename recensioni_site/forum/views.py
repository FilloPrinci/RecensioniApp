from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Sezione,SezioneImage
from .mixins import StaffMixing

# Create your views here.
class CreaSezione(CreateView):
    model = Sezione
    fields = ["nome_sezione", "descrizione", "citta", "provincia", "indirizzo", "logo_sezione"]
    template_name = "forum/crea_sezione.html"
    success_url = "/"

    def form_valid(self, form):
        print(self.request.user)
        form.instance.user_id = self.request.user.pk

        return super().form_valid(form)

def visualizzaSezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    immagini = SezioneImage.objects.filter(post=sezione)
    context = {"sezione": sezione, "immagini":immagini}
    return render(request, "forum/singola_sezione.html", context )

