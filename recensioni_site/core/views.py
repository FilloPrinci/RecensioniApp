from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from forum.models import Sezione
from django.views.generic.list import ListView

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



