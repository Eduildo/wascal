from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


GENDER_CHOICE = (
    (1, 'M'),
    (2, 'F'),
    (3, 'Autre'),
)

MARITAL_CHOICE = (
    (1, 'Célibataire'),
    (2, 'Marié'),
    (3, 'Autre'),
    
)

class Personne(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_naissance = models.DateTimeField(verbose_name="Date de naissance")
    lieu_naissance = models.CharField(max_length=40, verbose_name="Lieu de naissance")
    nationalite = models.CharField(max_length=40)
    telephone = models.IntegerField(verbose_name="Numero de telephone")
    email = models.EmailField(verbose_name="email")
    adresse = models.CharField(max_length=60, verbose_name="Adresse")
    etat_civil = models.PositiveSmallIntegerField(choices= MARITAL_CHOICE, default=1)
    photo = models.CharField(max_length=256, null=True)
    genre = models.PositiveSmallIntegerField(choices= GENDER_CHOICE, default=1)
    
    
    class Meta:
        abstract = True
        
MODE_CHOICES = (
        (1, 'admin'),
        (2, 'candidat'),
        (3, 'enseignant'),
        (4, 'etudiant'),
        (5, 'secretaire'),
        (6, 'rejecter'),
    )



class Filiere(models.Model):
  
    nom = models.CharField(max_length=100, verbose_name="Nom filiere")
    initial = models.CharField(max_length=100, verbose_name="Initial")
    
    
    class Meta:
        verbose_name_plural = "Filieres"
        
    def __str__(self):
        return self.nom


class AnneeAcademique(models.Model):
     
    date_debut = models.DateField(default=timezone.now, verbose_name="Date de debut")
    date_fin = models.DateField(default=timezone.now, verbose_name="Date fin")
    # debut = date_debut.unique_for_year
    # fin = str(date_fin)
    # cycle = fin
    
    class Meta:
        
        verbose_name_plural = "AnneeAcademique"
        
    def __str__(self):
        return self.date_debut.strftime('%Y')+ '/' +self.date_fin.strftime('%Y')
    
  
  
class Niveau(models.Model):
    
    niveau_academique = models.CharField(max_length=20)
    date_creation = models.DateField(default=timezone.now, verbose_name="Date de creation")
    
    class Meta:
        verbose_name_plural = "Niveau"
        
    def __str__(self):
        return self.niveau_academique
    
      

class Groupe(models.Model):
    
    #id = models.CharField(max_length=6, verbose_name="Id de groupe")
    nom_groupe = models.CharField(max_length=10, verbose_name="Nom de groupe")
    cycle = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date creation")
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Groupes"
        
    def __str__(self):
        return self.nom_groupe






    
class Etudiant(Personne):
    
    matricule = models.CharField(max_length=20, null=True, verbose_name="Matricule")
    prenom_contact = models.CharField(max_length=30)
    nom_contact = models.CharField(max_length=30)
    telephone_contact = models.IntegerField(verbose_name="Numero de telephone")
    email_contact = models.EmailField(verbose_name="email")
    ecole_provenance = models.CharField(max_length=30, verbose_name="Ecole de provenance")
    motivation = models.CharField(max_length=500, verbose_name="Motivation")
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date creation")
    niveau = models.ForeignKey(Niveau, default=1, on_delete=models.CASCADE)
    atestation = models.FileField()
    filiere = models.ForeignKey(Filiere, default=1, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Pour étendre l'utilisateur
    profil = models.PositiveSmallIntegerField(choices= MODE_CHOICES, default=2)
    status = models.CharField(max_length=20, default="pending" )
    groupe = models.ForeignKey(Groupe, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name_plural = "Etudiants"
        
    def __str__(self):
        """donne une represantation en chaine de caractere e de l'objet
        """
        return f'{self.prenom}{self.nom}'
    
 
  

class Enseignant(Personne):
    """[summary]
                Cette classe c'est pour recuperer les informations des enseignants
                il herite les attribut de classe abstrait personne
    Args:
        models ([type]): [description]
    """

    matricule = models.CharField(max_length=20, verbose_name="Matricule")
    specialite = models.CharField(max_length=20, verbose_name="Specialite")
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date creation")
    profil = models.PositiveSmallIntegerField(choices= MODE_CHOICES, default=3)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Enseignant" 
        
    def __str__(self):
        return self.nom    

class Responsable(Personne):
    """[summary]

    Args:
        models ([type]): [description]
    """
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date creation")
    
    class Meta:
        verbose_name_plural = "Responsable" 
        
    def __str__(self):
        return self.nom    

class Secretaire(Personne):
    """[summary]

    Args:
        models ([type]): [description]
    """
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date creation")
    
    class Meta:
        verbose_name_plural = "Secretaire" 
        
    def __str__(self):
        return self.nom
    
class Administrateur(Personne):
    """[summary]

    Args:
        models ([type]): [description]
    """
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date creation") 
    class Meta:
        verbose_name_plural = "Administrateur" 
        
    def __str__(self):
        return self.nom 
    

class Module(models.Model):
    
    nom_module = models.CharField(max_length=30, verbose_name="Nom Module")
    volume_horaire = models.IntegerField(verbose_name="Volume horaire")
    coefficient = models.IntegerField(verbose_name="Coefficient")
    
    class Meta:
        verbose_name_plural = "Modules"
        
    def __str__(self):
        return self.nom_module
    
    
    

    

class Semestre(models.Model):
    
    nom = models.DateField(default=timezone.now, verbose_name="Date de debut")
    date_debut = models.DateField(default=timezone.now, verbose_name="Date de debut")
    date_fin = models.DateField(default=timezone.now, verbose_name="Date fin")
    
    class Meta:
        verbose_name_plural = "Semestres"
        
    def __str__(self):
        return self.nom
    
    
class Evaluation(models.Model):
    
    type_evaluation = models.CharField(max_length=20, verbose_name="Type evaluation")
    date_evaluation = models.DateField(default=timezone.now, verbose_name="Date evaluation")
    numero = models.IntegerField(verbose_name="Numero evaluation")
    
    class Meta:
        verbose_name_plural = "Evaluations"
        
        def __str__(self):
            return self.type_evaluation
        
        
class InfoModule(models.Model):
    
    description = models.CharField(max_length=500, verbose_name="Information du module")
    
    class Meta:
        verbose_name_plural = "Informations module"
        
        def __str__(self):
            return self.description
        
class Chapitre(models.Model):
    titre = models.CharField(max_length=100, verbose_name="Chapitre")
    
    class Meta:
        verbose_name_plural = "Chapitres"
        
        def __str__(self):
            return self.titre
    

# Create your models here.
