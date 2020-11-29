from django.urls import path, include
from . import views

app_name = 'core'



urlpatterns = [
    path('', views.index, name='index'),
    path('admins', views.admins, name='admins'),
    path('new_user/', views.new_user, name='new_user'),
    path('login/', views.login, name='login'),
    path('admission/', views.admission, name='admission'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('formations', views.formations, name='formations'),
    
    
    #Routes for candidats
    path('candidats/', views.candidats, name='candidats'),
    path('candidat_info/<int:candidat_id>/', views.candidat_info, name='candidat_info'),
    path('accept_candidat/<int:candidat_id>/', views.accept_candidat, name='accept_candidat'),
    path('reject_candidat/<int:candidat_id>/', views.reject_candidat, name='reject_candidat'),
    path('accepted_candidat/', views.accepted_candidat, name='accepted_candidat'),
    path('candidats_rejecter/', views.candidats_rejecter, name='candidats_rejecter'),
    
    #Routes for students
    path('new_subscribers/', views.new_subscribers, name='new_subscribers'),
    
    
    path('get_filieres/', views.get_filieres, name='get_filieres'),
    path('all_groups/', views.all_groups, name='all_groups'),
    path('groupes/<int:filiere_id>/', views.groupes, name='groupes'),
    path('groupe_info/<int:groupe_id>/', views.groupe_info, name='groupe_info'),
    path('add_student_in_group/<int:groupe_id>/', views.add_student_in_group, name='add_student_in_group'),
    path('new_group/<int:filiere_id>/', views.new_group, name='new_group'),
    path('add_in_group/<int:groupe_id>/<int:etudiant_id>', views.add_in_group, name='add_in_group'),
    
   #Routes for teacher 
    path('enseignants/', views.enseignants, name='enseignants'),
    path('register_prof', views.register_prof, name="register_prof"),
    path('new_prof/', views.new_prof, name='new_prof'),
    path('prof_info/<int:prof_id>/', views.prof_info, name='prof_info'),
    path('prof_update/<int:prof_id>/', views.prof_update, name='prof_update'),
    
    
    
    
    
    # path('logintest/', views.logintest, name='logintest'),
    # path('candidat/', views.candidat, name='candidat'),
    # path('enseignant/', views.enseignant, name='enseignant'),
    # path('secretaire/', views.secretaire, name='secretaire'),
    # path('etudiant/', views.etudiant, name='etudiant'),    
]