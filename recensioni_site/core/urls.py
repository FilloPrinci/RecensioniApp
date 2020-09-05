from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.homeView, name='homepage'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('sezione/<int:pk>/modifica/', login_required(views.ArticoloChange.as_view()), name="articolo-modifica"),
    path('user/<username>/', views.userProfileView, name='user_profile'),
    path('articolo/<int:pk>/delete/', login_required(views.ArticleDelete.as_view()),  name='articolo-delete'),
    path('cerca/', login_required(views.cerca), name='cerca'),
    path('ricerca_avanzata/', views.ricerca_avanzata , name='ricerca_avanzata'),
    path('risultati/', views.risultati , name='risultati'),
]
