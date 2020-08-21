from django.db import models
from django.urls import reverse
from django.contrib.auth.models import  User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Sezione(models.Model):
    nome_sezione = models.CharField(max_length=80)
    descrizione = models.TextField(default='', null=False)
    citta = models.CharField(max_length=80,default='', null=False)
    provincia = models.CharField(max_length=80,default='', null=False)
    indirizzo = models.CharField(max_length=80,default='', null=False)


    logo_sezione = models.ImageField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome_sezione

    def get_absolute_url(self):
        return reverse("sezione_view", kwargs={"pk" : self.pk})

        
    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"

class SezioneImage(models.Model):
    post = models.ForeignKey(Sezione, on_delete=models.CASCADE,related_name='images')
    logo_sezione = models.ImageField(upload_to ='images/')

    def __str__(self):
        return self.post.nome_sezione

class Post(models.Model):
    autore_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    contenuto = models.TextField()
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    data_creazione = models.DateTimeField(auto_now_add=True)
    sezione = models.ForeignKey(Sezione, on_delete=models.CASCADE)

    def __str__(self):
        return self.autore_post.username

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    
