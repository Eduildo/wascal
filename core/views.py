from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login as auth_login, authenticate

from .forms import GroupeForms, EnseignantForms, SignUpForm

from core.models import Etudiant, Enseignant, Secretaire, Filiere, Groupe

# Web site Views
def index(request):
    return render(request, 'portail/index.html')


def admission(request):
    return render(request, 'portail/admissions.html')

def contact(request):
    return render(request, 'portail/contact.html')

def about(request):
    return render(request, 'portail/about.html')


def formations(request):
    return render(request, 'portail/courses.html')

# Fin Web site Views


# PLATEFORME VIEWS

# Dasheboard admin
def admins(request):
    all_candidats = Etudiant.objects.all().filter(status='pending').count()
    new_etudiant = Etudiant.objects.all().filter(status='accepted').count()
    context = {'all_candidats': all_candidats, 'new_etudiant': new_etudiant}
    return render(request, 'admins/index.html', context)

# Dasheboard candidat
def candidat(request):
    return render(request, 'candidat/index.html')

# Dasheboard admin
def enseignant(request):
    return render(request, 'enseignant/index.html')


def etudiant(request):
    return render(request, 'etudiant/index.html')


def new_user(request):
   #New user cette methode vas faire la redirection de vers la page d'inscription
    return redirect('authentication:register_user')
        
   

def login(request):
    # New user cette methode vas faire la redirection de vers la page de connexion 
    # que se trouve dans authenticate
    return redirect('authentication:login_view')
    #return render(request, 'portail/login.html')
    
    
    
# =============== GESTION DES CANDIDATS ==================
  
  # Liste de tous les candidats  
def candidats(request):
    all_candidats = Etudiant.objects.all().filter(status='pending').count()
    candidats = Etudiant.objects.all().filter(profil=2)
    context = {'candidats': candidats, 'all_candidats': all_candidats}
    return render(request, 'admins/candidats.html', context)

# Information de candidat
def candidat_info(request, candidat_id):
    candidat = Etudiant.objects.get(id=candidat_id)
    context = {'candidat': candidat}
    return render(request, 'admins/candidat_info.html', context )

# La fonction pour accepcter un candidat
def accept_candidat(request, candidat_id):
    chaine = 'MST00'
    all_candidats = Etudiant.objects.all().filter(profil=2).count()
    numero = 1 + all_candidats
    candidat = Etudiant.objects.get(id=candidat_id)
    candidat.profil = 4
    candidat.status = 'accepted'
    matricule = chaine + str(numero)
    candidat.matricule = matricule
    candidat.save()
    user_id = candidat.user.id
    user = User.objects.get(id=user_id)
    user.groups.clear() 
    my_group = Group.objects.get(name='etudiant') 
    my_group.user_set.add(user)
    user.save()
    user.groups.all()
    return redirect('core:candidats')

# La fonction pour rejecter un candidat
def reject_candidat(request, candidat_id):
    candidat = Etudiant.objects.get(id=candidat_id)
    candidat.status = 'rejected'
    candidat.profil = 6
    candidat.save()
    return redirect('core:candidats')

# La fonction pour lister les candidats accepcter
def accepted_candidat(request):
    acceptee = Etudiant.objects.all().filter(status='accepted')
    context = {'acceptee': acceptee}
    return render(request, 'admins/candidats_accepter.html', context)

# candidats non aceptés
def candidats_rejecter(request):
    candidats = Etudiant.objects.all().filter(status='rejected')
    context = {'candidats': candidats}
    return render(request, 'admins/candidats_rejecter.html', context)


# ============= FIN GESTION DES CANDIDATS ==================


# =============== GESTION DES FILIERES ET GROUPES =======================

# pour recuperer tous les filieres
def get_filieres(request):
    filieres = Filiere.objects.order_by('initial')
    context = {'filieres': filieres}
    return render(request, 'admins/filiers.html', context)

# Liste de tous les groupes de systeme
def all_groups(request):
    groupes = Groupe.objects.order_by('filiere')
    context = {'groupes': groupes}
    return render(request, 'admins/all_groups.html', context)

# Pour recuperer les groupes dans une filière
def groupes(request, filiere_id):
    filiere = Filiere.objects.get(id=filiere_id)
    groupes = Groupe.objects.all().filter(filiere=filiere_id)
    context = {'groupes': groupes, 'filiere': filiere}
    return render(request, 'admins/groupes.html', context)


#Pour creer un nouveau groupe
def new_group(request, filiere_id):
    filiere = Filiere.objects.get(id=filiere_id)
    if request.method != 'POST': 
        form = GroupeForms()   
    else: 
        form = GroupeForms(data = request.POST)
        if form.is_valid():
            groupe = form.save(commit=False)
            groupe.filiere = filiere
            groupe.save()
            return redirect('core:groupes', filiere_id = filiere.id )
        else:
            form = GroupeForm()
    context = {'form': form, 'filiere': filiere}
    return render(request, 'admins/new_group.html', context)


#Informations de groupe

def groupe_info(request, groupe_id): 
    groupe = Groupe.objects.get(id=groupe_id)
    etudiants = Etudiant.objects.all().filter(status='accepted').filter(filiere=groupe.filiere).filter(groupe=groupe_id)
    all_students = Etudiant.objects.all().filter(groupe=groupe_id).count()
    context = {'groupe': groupe, 'etudiants': etudiants, 'all_students': all_students}
    return render(request, 'admins/groupe_info.html', context)


#acceptee = Etudiant.objects.all().filter(groupe=groupe_id)


def add_student_in_group(request, groupe_id):
    groupe = Groupe.objects.get(id=groupe_id)
    acceptee = Etudiant.objects.all().filter(status='accepted').filter(filiere=groupe.filiere).filter(groupe=None)
    context = {'groupe': groupe, 'acceptee': acceptee}
    return render(request, 'admins/add_student_in_group.html', context)



def add_in_group(request, groupe_id, etudiant_id ):
    etudiant = Etudiant.objects.get(id=etudiant_id)
    groupe = Groupe.objects.get(id=groupe_id)
    etudiant.groupe = groupe
    etudiant.save()
    return redirect('core:add_student_in_group', groupe_id = groupe.id)
    


# ============= FIN GESTION DES FILIERES ET GROUPES ======================
   
   
   
# =============== GESTION DES ETUDIANTS =======================

# Liste des nouveaux etudiants
def new_subscribers(request):
    acceptee = Etudiant.objects.all().filter(status='accepted')
    context = {'acceptee': acceptee}
    return render(request, 'admins/new_subscribers.html', context)

# ============= FIN GESTION DES ETUDIANTS =======================
    

# =============== GESTION DES ENSEIGNANTS =======================

def enseignants(request):
    enseignants = Enseignant.objects.order_by('specialite')
    context = {'enseignants': enseignants}
    return render(request, 'admins/enseignants.html', context)


def register_prof(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            #auth_login(request, user)
            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            prof_group = Group.objects.get_or_create(name='enseignant')
            prof_group[0].user_set.add(user)
            return redirect('core:new_prof')
        else:
            form = SignUpForm()    
    else:
        form = SignUpForm()

    return render(request, "admins/register_prof.html", {"form": form, "msg" : msg, "success" : success })



def new_prof(request):
    profil = User.objects.latest('id')
    if request.method != 'POST':
        form = EnseignantForms()
    else:
        form = EnseignantForms(request.POST)
        if form.is_valid():
            enseignant = form.save(commit=False)
            enseignant.user = profil
            enseignant.save()
            return redirect('core:enseignants')
    context = {'form': form}
    return render(request, 'admins/new_prof.html', context )


def prof_info(request, prof_id):
    prof = Enseignant.objects.get(id=prof_id)
    context = {'prof': prof}
    return render(request, 'admins/prof_info.html', context)

def prof_update(request, prof_id):
    prof = Enseignant.objects.get(id=prof_id)
    if request.method != 'POST':
        form = EnseignantForms(instance=prof)
    else:
        form = EnseignantForms(instance=prof, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:enseignants')
    context = {'prof': prof, 'form': form}
    return render(request, 'admins/prof_update.html', context)
# ============= FIN GESTION DES ENSEIGNANTS =====================

# FIM PLATEFORME VIEWS
