from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .forms import DiscussioneModelForm
from .models import Post, Sezione
from .mixins import StaffMixing

# Create your views here.
class CreaSezione(StaffMixing, CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url = "/"

def visualizzaSezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    context = {"sezione": sezione}
    return render(request, "forum/singola_sezione.html", context )

def creaDiscussione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    if (request.method == 'POST'):
        form = DiscussioneModelForm(request.POST)
        if form.is_valid():
            discussione = form.save(commit=False)
            discussione.sezione_appartenenza = sezione
            discussione.autore_discussione = request.user
            discussione.save()
            primo_post = Post.objects.create(discussione=discussione, autore_post=request.user, contenuto=form.cleaned_data["contenuto"])
            return HttpResponseRedirect("/admin/")
    else:
        form = DiscussioneModelForm()
    context = {"form": form, "sezione":sezione}
    return render(request, "forum/crea_discussioni.html", context)

