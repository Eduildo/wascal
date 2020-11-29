from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Groupe, Enseignant



class GroupeForms(forms.ModelForm):
    
    class Meta:
        
        model = Groupe
        fields = ('nom_groupe', 'cycle', 'niveau')
        
    
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  
        
class EnseignantForms(forms.ModelForm):
    
    class Meta:
        
        model = Enseignant
        fields = ['nom', 'prenom', 'date_naissance', 'lieu_naissance', 'nationalite', 'telephone', 'email', 'adresse', 'etat_civil' , 'specialite']


    