from django.db import models
from django.urls import reverse
from django.contrib.auth.models import  User
# Create your models here.

class Sezione(models.Model):
    nome_sezione = models.CharField(max_length=80)
    descrizione = models.TextField(default='', null=False)
    citta = models.CharField(max_length=80,default='', null=False)
    provincia = models.CharField(max_length=80,default='', null=False)
    indirizzo = models.CharField(max_length=80,default='', null=False)
   

    logo_sezione = models.ImageField(blank=True, null=True)

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

    
