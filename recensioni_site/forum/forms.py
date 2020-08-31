from django import forms
from .models import Sezione, Post

class DiscussioneModelForm(forms.ModelForm):
    contenuto = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Di cosa vuoi parlarci"}),
        max_length=4000, label = "Primo Messaggio")

    class Meta:
        model = Sezione
        fields = ["nome_sezione", "descrizione"]
        widget = {
            "nome_sezione": forms.TextInput(attrs={"placeholder": "Titolo dell'articolo "})
        }

class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["contenuto", "rating"]