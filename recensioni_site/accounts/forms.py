from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormRegistrazione(UserCreationForm):
    email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput())
    proprietario = forms.BooleanField(required=False)
    notifiche = forms.IntegerField(initial=0, required=False)
    indirizzo_notifiche = forms.CharField(initial="", required=False)



    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'notifiche': forms.HiddenInput()}
        widgets = {'indirizzo_notifiche': forms.HiddenInput()}