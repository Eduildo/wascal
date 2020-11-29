# Generated by Django 3.1.3 on 2020-11-20 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_naissance', models.DateTimeField(verbose_name='Date de naissance')),
                ('lieu_naissance', models.CharField(max_length=40, verbose_name='Lieu de naissance')),
                ('nationalite', models.CharField(max_length=40)),
                ('telephone', models.IntegerField(verbose_name='Numero de telephone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('adresse', models.CharField(max_length=60, verbose_name='Adresse')),
                ('etat_civil', models.PositiveSmallIntegerField(choices=[(1, 'Célibataire'), (2, 'Marié'), (3, 'Autre')], default=1)),
                ('photo', models.CharField(max_length=256, null=True)),
                ('genre', models.PositiveSmallIntegerField(choices=[(1, 'M'), (2, 'F'), (3, 'Autre')], default=1)),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date creation')),
            ],
            options={
                'verbose_name_plural': 'Administrateur',
            },
        ),
        migrations.CreateModel(
            name='AnneeAcademique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(default=django.utils.timezone.now, verbose_name='Date de debut')),
                ('date_fin', models.DateField(default=django.utils.timezone.now, verbose_name='Date fin')),
            ],
            options={
                'verbose_name_plural': 'AnneeAcademique',
            },
        ),
        migrations.CreateModel(
            name='Chapitre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, verbose_name='Chapitre')),
            ],
            options={
                'verbose_name_plural': 'Chapitres',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_evaluation', models.CharField(max_length=20, verbose_name='Type evaluation')),
                ('date_evaluation', models.DateField(default=django.utils.timezone.now, verbose_name='Date evaluation')),
                ('numero', models.IntegerField(verbose_name='Numero evaluation')),
            ],
            options={
                'verbose_name_plural': 'Evaluations',
            },
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom filiere')),
                ('initial', models.CharField(max_length=100, verbose_name='Initial')),
            ],
            options={
                'verbose_name_plural': 'Filieres',
            },
        ),
        migrations.CreateModel(
            name='InfoModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, verbose_name='Information du module')),
            ],
            options={
                'verbose_name_plural': 'Informations module',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_module', models.CharField(max_length=30, verbose_name='Nom Module')),
                ('volume_horaire', models.IntegerField(verbose_name='Volume horaire')),
                ('coefficient', models.IntegerField(verbose_name='Coefficient')),
            ],
            options={
                'verbose_name_plural': 'Modules',
            },
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau_academique', models.CharField(max_length=20)),
                ('date_creation', models.DateField(default=django.utils.timezone.now, verbose_name='Date de creation')),
            ],
            options={
                'verbose_name_plural': 'Niveau',
            },
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_naissance', models.DateTimeField(verbose_name='Date de naissance')),
                ('lieu_naissance', models.CharField(max_length=40, verbose_name='Lieu de naissance')),
                ('nationalite', models.CharField(max_length=40)),
                ('telephone', models.IntegerField(verbose_name='Numero de telephone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('adresse', models.CharField(max_length=60, verbose_name='Adresse')),
                ('etat_civil', models.PositiveSmallIntegerField(choices=[(1, 'Célibataire'), (2, 'Marié'), (3, 'Autre')], default=1)),
                ('photo', models.CharField(max_length=256, null=True)),
                ('genre', models.PositiveSmallIntegerField(choices=[(1, 'M'), (2, 'F'), (3, 'Autre')], default=1)),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date creation')),
            ],
            options={
                'verbose_name_plural': 'Responsable',
            },
        ),
        migrations.CreateModel(
            name='Secretaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_naissance', models.DateTimeField(verbose_name='Date de naissance')),
                ('lieu_naissance', models.CharField(max_length=40, verbose_name='Lieu de naissance')),
                ('nationalite', models.CharField(max_length=40)),
                ('telephone', models.IntegerField(verbose_name='Numero de telephone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('adresse', models.CharField(max_length=60, verbose_name='Adresse')),
                ('etat_civil', models.PositiveSmallIntegerField(choices=[(1, 'Célibataire'), (2, 'Marié'), (3, 'Autre')], default=1)),
                ('photo', models.CharField(max_length=256, null=True)),
                ('genre', models.PositiveSmallIntegerField(choices=[(1, 'M'), (2, 'F'), (3, 'Autre')], default=1)),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date creation')),
            ],
            options={
                'verbose_name_plural': 'Secretaire',
            },
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.DateField(default=django.utils.timezone.now, verbose_name='Date de debut')),
                ('date_debut', models.DateField(default=django.utils.timezone.now, verbose_name='Date de debut')),
                ('date_fin', models.DateField(default=django.utils.timezone.now, verbose_name='Date fin')),
            ],
            options={
                'verbose_name_plural': 'Semestres',
            },
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_groupe', models.CharField(max_length=10, verbose_name='Nom de groupe')),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date creation')),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.anneeacademique')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.filiere')),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.niveau')),
            ],
            options={
                'verbose_name_plural': 'Groupes',
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_naissance', models.DateTimeField(verbose_name='Date de naissance')),
                ('lieu_naissance', models.CharField(max_length=40, verbose_name='Lieu de naissance')),
                ('nationalite', models.CharField(max_length=40)),
                ('telephone', models.IntegerField(verbose_name='Numero de telephone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('adresse', models.CharField(max_length=60, verbose_name='Adresse')),
                ('etat_civil', models.PositiveSmallIntegerField(choices=[(1, 'Célibataire'), (2, 'Marié'), (3, 'Autre')], default=1)),
                ('photo', models.CharField(max_length=256, null=True)),
                ('genre', models.PositiveSmallIntegerField(choices=[(1, 'M'), (2, 'F'), (3, 'Autre')], default=1)),
                ('matricule', models.CharField(max_length=20, null=True, verbose_name='Matricule')),
                ('prenom_contact', models.CharField(max_length=30)),
                ('nom_contact', models.CharField(max_length=30)),
                ('telephone_contact', models.IntegerField(verbose_name='Numero de telephone')),
                ('email_contact', models.EmailField(max_length=254, verbose_name='email')),
                ('ecole_provenance', models.CharField(max_length=30, verbose_name='Ecole de provenance')),
                ('motivation', models.CharField(max_length=500, verbose_name='Motivation')),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date creation')),
                ('atestation', models.FileField(upload_to='')),
                ('profil', models.PositiveSmallIntegerField(choices=[(1, 'admin'), (2, 'candidat'), (3, 'enseignant'), (4, 'etudiant'), (5, 'secretaire'), (6, 'rejecter')], default=2)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('filiere', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.filiere')),
                ('groupe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.groupe')),
                ('niveau', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.niveau')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Etudiants',
            },
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_naissance', models.DateTimeField(verbose_name='Date de naissance')),
                ('lieu_naissance', models.CharField(max_length=40, verbose_name='Lieu de naissance')),
                ('nationalite', models.CharField(max_length=40)),
                ('telephone', models.IntegerField(verbose_name='Numero de telephone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('adresse', models.CharField(max_length=60, verbose_name='Adresse')),
                ('etat_civil', models.PositiveSmallIntegerField(choices=[(1, 'Célibataire'), (2, 'Marié'), (3, 'Autre')], default=1)),
                ('photo', models.CharField(max_length=256, null=True)),
                ('genre', models.PositiveSmallIntegerField(choices=[(1, 'M'), (2, 'F'), (3, 'Autre')], default=1)),
                ('matricule', models.CharField(max_length=20, verbose_name='Matricule')),
                ('specialite', models.CharField(max_length=20, verbose_name='Specialite')),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date creation')),
                ('profil', models.PositiveSmallIntegerField(choices=[(1, 'admin'), (2, 'candidat'), (3, 'enseignant'), (4, 'etudiant'), (5, 'secretaire'), (6, 'rejecter')], default=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Enseignant',
            },
        ),
    ]
