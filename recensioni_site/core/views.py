from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
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

def cerca(request, ):
    '''
    Barra di ricerca
    :return: ritorna la pagina che mostra i risultati della ricerca
    '''
    if "q" in request.GET:
        querystring = request.GET.get("q")
        # print(querystring)
        if len(querystring) == 0:
            return redirect("/cerca/")
        sezioni = Sezione.objects.filter(nome_sezione__icontains=querystring)
        print(sezioni)
        context = {"sezioni": sezioni}
        return render(request, 'core/cerca.html', context)
    else:
        return render(request, 'core/cerca.html')

def ricerca_avanzata(request, ):
    return render(request, 'core/ricerca_avanzata.html')

def risultati(request, ):
    '''
    Barra di ricerca
    :return: ritorna la pagina che mostra i risultati della ricerca
    '''

    if "cosa" in request.GET:
        querystring = request.GET.get("cosa")
        sezioni = Sezione.objects.filter(nome_sezione__icontains=querystring)
    else:
        querystring = ""
    print(querystring)


    if "tipo1"  in request.GET:
        tipo1 = request.GET.get("tipo1")
        sezioni = sezioni.exclude(hotelB=False)
    else:
        tipo1 = "False"
    print(tipo1)

    if "tipo2"  in request.GET:
        tipo2 = request.GET.get("tipo2")
        sezioni = sezioni.exclude(ristoranteB=False)
    else:
        tipo2 = "False"
    print(tipo2)

    if "tipo3"  in request.GET:
        tipo3 = request.GET.get("tipo3")
        sezioni = sezioni.exclude(fastFoodB=False)
    else:
        tipo3 = "False"
    print(tipo3)

    if "tipo4"  in request.GET:
        tipo4 = request.GET.get("tipo4")
        sezioni = sezioni.exclude(casaVacanzaB=False)
    else:
        tipo4 = "False"
    print(tipo4)

    if "tipo5"  in request.GET:
        tipo5 = request.GET.get("tipo5")
        sezioni = sezioni.exclude(agriturismoB=False)
    else:
        tipo5 = "False"
    print(tipo5)

    print("risultao : " + str(sezioni))

    context = {"sezioni": sezioni}

    return render(request, 'core/risultati.html', context)

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