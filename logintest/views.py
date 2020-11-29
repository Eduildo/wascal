from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from core.models import Etudiant, Enseignant, Secretaire


   # Verification de differents profils
def is_candidat(user):
    return user.groups.filter(name='candidat').exists()
def is_etudiant(user):
    return user.groups.filter(name='etudiant').exists()
def is_enseignant(user):
    return user.groups.filter(name='enseignant').exists()
def is_secretaire(user):
    return user.groups.filter(name='secretaire').exists()
def is_admin(user):
    return user.groups.filter(name='admin').exists()



def index(request):
    if is_admin(request.user):
        group = User.objects.filter(groups = 1)
        all_candidats = Etudiant.objects.all().filter(status='pending').count()
        new_etudiant = Etudiant.objects.all().filter(status='accepted').count()
        context = {'group': group, 'all_candidats': all_candidats, 'new_etudiant': new_etudiant}
        return render(request, 'admins/index.html', context)
    elif is_candidat(request.user):
        accountapproval= Etudiant.objects.all().filter(user_id=request.user.id)
        if accountapproval:
            group = User.objects.filter(groups = 2)
            context = {'group': group}
            return render(request, 'candidat/index.html', context)
        else:
            return render(request, 'elearning/index.html')
    elif is_etudiant(request.user):
        accountapproval=Etudiant.objects.all().filter(user_id=request.user.id)
        if accountapproval:
            group = User.objects.filter(groups = 4)
            context = {'group': group}
            return render(request, 'etudiant/index.html')
        else:
            return render(request, 'elearning/index.html')
    elif is_enseignant(request.user):
        accountapproval=Enseignant.objects.all().filter(user_id=request.user.id)
        if accountapproval:
            group = User.objects.filter(groups = 3)
            context = {'group': group}
            return render(request, 'enseignant/index.html', context)
        else:
            return render(request, 'elearning/index.html')
    elif is_secretaire(request.user):
        accountapproval=Secretaire.objects.all().filter(user_id=request.user.id)
        if accountapproval:
            group = User.objects.filter(groups = 5)
            context = {'group': group}
            return render(request, 'secretaire/index.html')
        else:
            return render(request, 'elearning/index.html')
