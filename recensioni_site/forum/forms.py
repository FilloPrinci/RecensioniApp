from django import forms
from .models import Discussione, Post

class DiscussioneModelForm(forms.ModelForm):
    contenuto = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Di cosa vuoi parlarci"}),
        max_length=4000, label = "Primo Messaggio")

    class Meta:
        model = Discussione
        fields = ["titolo", "contenuto"]
        widget = {
            "titolo": forms.TextInput(attrs={"placeholder": "Titolo della discussione"})
        }

class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["contenuto"]