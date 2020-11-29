from django.contrib import admin
from core.models import Etudiant, Niveau, Filiere, Groupe, AnneeAcademique, Enseignant

admin.site.register(Niveau)
admin.site.register(Etudiant)
admin.site.register(Filiere)
admin.site.register(Groupe)
admin.site.register(AnneeAcademique)
admin.site.register(Enseignant)

# Register your models here.
