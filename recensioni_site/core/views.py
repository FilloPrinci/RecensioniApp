from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from forum.models import Sezione
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView, DetailView, FormView
from forum.views import visualizzaSezione
from django.urls import reverse_lazy
# Create your views here.

class HomeView(ListView):
    queryset = Sezione.objects.all()
    template_name = 'core/homepage.html'
    context_object_name = "lista_sezioni"

class UserList(ListView):
    model = User
    template_name = 'core/users.html'

def homepage(request):
    return render(request, 'core/homepage.html')

def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    sezione = Sezione.objects.filter(user=user.pk).order_by("-pk")
    context={"user": user, "sezioni":sezione}
    return render(request, 'core/user_profile.html', context)


class ArticoloChange(UpdateView):
    '''
    Modifica il titolo dell'articolo
    '''
    model = Sezione
    fields = ("nome_sezione", "descrizione", "citta",
              "provincia", "indirizzo", "logo_sezione")
    template_name = 'core/modifica.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        articleid = self.kwargs['pk']
        articolo = get_object_or_404(Sezione, id=articleid)

        if user.id is not articolo.user.id:
            return visualizzaSezione(request, articleid)

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        articleid = self.kwargs['pk']
        articolo = get_object_or_404(Sezione, id=articleid)
        user = get_object_or_404(User, username=articolo.user)
        return reverse_lazy('user_profile', kwargs={'username': user})


class ArticleDelete(DeleteView):
    '''
    Eliminazione di un articolo
    '''
    model = Sezione
    template_name = 'core/deletearticle.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        articleid = self.kwargs['pk']
        articolo = get_object_or_404(Sezione, id=articleid)

        if user.id is not articolo.user.id:
            return visualizzaSezione(request, articleid)

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        articleid = self.kwargs['pk']
        articolo = get_object_or_404(Sezione, id=articleid)
        user = get_object_or_404(User, username=articolo.user)
        return reverse_lazy('user_profile', kwargs={'username': user})

