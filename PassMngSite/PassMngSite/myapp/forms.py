# en file baraye sefareshi kardane form ha va field haye db ast.
from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput
from cryptography.fernet import Fernet #encode & decode passwords


class ContactForm(forms.Form):  # en class automat code html 3 field zir ra ejad mikinad.
        subject = forms.CharField(required=False, max_length=15)
        email = forms.EmailField(label='E-mail')  # pishfarz ejbari ast..
        message = forms.CharField(widget=forms.Textarea)


class ChangePassword(BSModalForm): #Inherits PopRequestMixin and Django’s forms.Form
    title = forms.CharField(widget=forms.TextInput())
    old_pass = forms.CharField(widget= forms.PasswordInput,max_length=10,help_text='oldd password')
    new_pass1 = forms.CharField(widget= forms.PasswordInput,max_length=10,help_text='new password')
    new_pass2 = forms.CharField(widget= forms.PasswordInput,max_length=10,help_text='repeatation of new password')


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
