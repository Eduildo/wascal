# Generated by Django 3.1.3 on 2020-12-06 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_module_enseignant'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='groupe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.groupe'),
            preserve_default=False,
        ),
    ]