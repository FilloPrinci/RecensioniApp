from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Sezione,SezioneImage, UserDataReccomandation
from .forms import DiscussioneModelForm, PostModelForm
from django.contrib.auth.models import User
from .models import Post, Sezione
import json
from .mixins import StaffMixing

# Create your views here.
class CreaSezione(CreateView):
    model = Sezione
    fields = ["nome_sezione", "descrizione", "citta", "provincia", "indirizzo", "logo_sezione", "hotelB", "ristoranteB", "fastFoodB", "casaVacanzaB", "agriturismoB"]
    template_name = "forum/crea_sezione.html"
    success_url = "/"



    def form_valid(self, form):

        print(self.request.user)
        form.instance.user_id = self.request.user.pk

        form.save()
        if not self.request.user.is_staff:
            raise Http404
        return super().form_valid(form)

def visualizzaSezione(request, pk):

    if "cliccato" in request.GET:
        is_cliccato = request.GET.get("cliccato")
        print(is_cliccato)

        if (is_cliccato == "True"):
            request.user.first_name = "0"
            request.user.last_name = ""
            request.user.save()
            print(request.user.first_name)


    sezione = get_object_or_404(Sezione, pk=pk)
    posts_discussione = Post.objects.filter(sezione=sezione)

    if request.user.is_authenticated:

        for post in posts_discussione:
                setattr(post,'total_likes',post.total_likes())
                checkifPostLikeExists = Post.objects.filter(
                    id=post.id, likes=request.user).exists()
                if(checkifPostLikeExists):
                    setattr(post,'viewButton','btn-outline-danger')
                else:
                    setattr(post,'viewButton','btn-danger')
    else:
        for post in posts_discussione:
                setattr(post,'total_likes',post.total_likes())

                setattr(post,'viewButton','btn-danger disabled')
            

    tot_rating = 0
    n_rating = 0
    media_rating_reale = 0

    if(len(posts_discussione) == 0):
        media_rating = 0
    else:
        for post in posts_discussione:
            tot_rating += post.rating
            n_rating += 1
        media_rating = tot_rating / n_rating

    media_rating_reale = media_rating
    media_rating = int(round(media_rating))

    form_risposta = PostModelForm()
    immagini = SezioneImage.objects.filter(post=sezione)
    context = {"sezione": sezione, "immagini":immagini, "posts_discussione":posts_discussione, "form_risposta":form_risposta, "media_rating":media_rating, "media_rating_reale":media_rating_reale}
    return render(request, "forum/singola_sezione.html", context )

def aggiungiRisposta(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)

    listUsrDR = UserDataReccomandation.objects.filter(user=request.user)
    if not (listUsrDR.count() > 0):
        usrDR = UserDataReccomandation.objects.create(hotel=0, ristorante=0, fastFood=0, casaVacanza=0, agriturismo =0, user=request.user)
    else:
        usrDR = get_object_or_404(UserDataReccomandation, user=request.user)

    if (request.method == "POST"):
        form = PostModelForm(request.POST)
        if (form.is_valid()):
            form.save(commit=False)
            form.instance.sezione = sezione
            form.instance.autore_post = request.user
            form.save()
            url_discussione = reverse("sezione_view", kwargs={"pk": pk})

            user = get_object_or_404(User, pk=sezione.user.pk)
            if (user.first_name== ""):
                numero = 0
            else:
                numero = int(user.first_name)
            numero += 1
            user.first_name = str(numero)

            if(user.last_name == ""):
                notifiche = [{"user_post":request.user.username, "sezione_commentata":sezione.nome_sezione, "sezione_url":url_discussione}]
                user.last_name = json.dumps(notifiche)
            else:
                temp = json.loads(user.last_name)
                temp.append({"user_post":request.user.username, "sezione_commentata":sezione.nome_sezione, "sezione_url":url_discussione})
                user.last_name = json.dumps(temp)

            if (sezione.hotelB):
                usrDR.hotel += form.instance.rating
            if (sezione.ristoranteB):
                usrDR.ristorante += form.instance.rating
            if (sezione.fastFoodB):
                usrDR.fastFood += form.instance.rating
            if (sezione.casaVacanzaB):
                usrDR.casaVacanza += form.instance.rating
            if (sezione.agriturismoB):
                usrDR.agriturismo += form.instance.rating

            usrDR.save()
            user.save()

            print("numero di notifiche tot: " + user.first_name)
            print("lista urls: " + user.last_name)

            return HttpResponseRedirect(url_discussione)
    else:
        return HttpResponseBadRequest()


def likeView(request, pk):
    checkifPostLikeExists = Post.objects.filter(
        id=request.POST.get('post_id'), likes=request.user).exists()
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    print(post)
    if (checkifPostLikeExists):
        post.likes.remove(request.user)
        
    else:
        post.likes.add(request.user)

    url_discussione = reverse("sezione_view", kwargs={"pk": post.sezione.pk})
    return HttpResponseRedirect(url_discussione)


