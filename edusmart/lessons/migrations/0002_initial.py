# Generated by Django 5.2 on 2025-06-18 23:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_initial'),
        ('lessons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='estadorecursoleccion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grupoleccion',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.curso'),
        ),
        migrations.AddField(
            model_name='leccion',
            name='grupo_leccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.grupoleccion'),
        ),
        migrations.AddField(
            model_name='leccionusuario',
            name='leccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.leccion'),
        ),
        migrations.AddField(
            model_name='leccionusuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recursoleccion',
            name='leccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.leccion'),
        ),
        migrations.AddField(
            model_name='estadorecursoleccion',
            name='recurso_leccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.recursoleccion'),
        ),
    ]
