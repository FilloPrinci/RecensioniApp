from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Sezione,SezioneImage
from .forms import DiscussioneModelForm, PostModelForm
from .models import Post, Sezione
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
    posts_discussione = Post.objects.filter(sezione=sezione)
    form_risposta = PostModelForm()
    immagini = SezioneImage.objects.filter(post=sezione)
    context = {"sezione": sezione, "immagini":immagini, "posts_discussione":posts_discussione, "form_risposta":form_risposta}
    return render(request, "forum/singola_sezione.html", context )

def aggiungiRisposta(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    if (request.method == "POST"):
        form = PostModelForm(request.POST)
        if (form.is_valid()):
            form.save(commit=False)
            form.instance.sezione = sezione
            form.instance.autore_post = request.user
            form.save()
            url_discussione = reverse("sezione_view", kwargs={"pk": pk})
            print("ciao")
            print("url da stampare :  "  + url_discussione)
            return HttpResponseRedirect(url_discussione)
    else:
        return HttpResponseBadRequest()

