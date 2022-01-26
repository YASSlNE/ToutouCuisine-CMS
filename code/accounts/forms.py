from pdb import post_mortem
from random import choices
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from bootstrap_datepicker_plus.widgets import DatePickerInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
# class CommandeForm2(forms.ModelForm):

class ClientForm(forms.Form):
    full_name=forms.CharField(label='Nom complet',max_length=100)
    num_tel=forms.CharField(label='Numero du telephone',max_length=50)
    lien_prof=forms.CharField(label='Lien du profile',max_length=200)
class CommandeForm(forms.Form):
    about=forms.CharField(label='Sujet/Theme',max_length=300)
    cout=forms.FloatField(label='Cout du commande')
    prix=forms.FloatField(label='Prix du commande')
    # date=forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     }))
    # cli=forms.ChoiceField()
#     c=Clients.objects.all()
#     # print(c)
#     big_list=[]
#     small_list=[]
#     for client in c:
#         small_list.append(client.id)
#         small_list.append(client.name)
#         big_list.append(tuple(small_list))
#         small_list=[]
#     choices=tuple(big_list)
# class CommandeForm(forms.ModelForm):
#     # post=forms.CharField(widget=forms.TextInput(
#     #     attrs={
#     #         'class':'form-control',
#     #     }
#     # ))

#     about=forms.CharField(label='Sujet/Theme',max_length=300)
#     cout=forms.FloatField(label='Cout du commande')
#     prix=forms.FloatField(label='Prix du commande')
#     # date=forms.DateTimeField(widget=DatePickerInput(format='%m/%d/%Y'))
#     # widget=forms.DateTimeInput(attrs={
#     #     'class': 'form-control datetimepicker-input',
#     #     'data-target': '#datetimepicker1',
#     #     # 'style':'width=20px'
#     # }))
#     class Meta:
#         model=Commande
#         fields=()
    # CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    # choices = forms.ChoiceField(help_text="Estado", choices=CHOICES)
    # field = forms.ChoiceField(label='Client',choices=choices)
    