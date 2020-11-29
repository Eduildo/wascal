# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User, Group
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, EtudiantForms
from core.models import Etudiant, Enseignant, Secretaire





def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('logintest:index')
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "portail/login.html", {"form": form, "msg" : msg})


def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            candidat_group = Group.objects.get_or_create(name='candidat')
            candidat_group[0].user_set.add(user)
            return redirect('authentication:new_candidat')

        else:
            form = SignUpForm()    
    else:
        form = SignUpForm()

    return render(request, "portail/register.html", {"form": form, "msg" : msg, "success" : success })


def new_candidat(request):
    profil = User.objects.latest('id')
    if request.method != 'POST':
        form = EtudiantForms()
    else:
        form = EtudiantForms(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save(commit=False)
            candidat.user = profil
            candidat.save()
            return redirect('core:login')
    context = {'form': form}
    return render(request, 'portail/inscription.html', context )




