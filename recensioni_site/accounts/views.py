from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.forms import FormRegistrazione

# Create your views here.

def resgistrazioneView(request):
    if request.method =="POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            proprietario = form.cleaned_data["proprietario"]
            notifiche = form.cleaned_data["notifiche"]
            indirizzo_notifiche = form.cleaned_data["indirizzo_notifiche"]

            User.objects.create_user(username=username, password=password, email=email, is_staff=proprietario, first_name=notifiche, last_name=indirizzo_notifiche)
            user = authenticate(username= username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = FormRegistrazione()

    context = {"form": form}
    return render(request, 'accounts/registrazione.html', context)