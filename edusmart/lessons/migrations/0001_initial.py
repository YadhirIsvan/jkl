# Generated by Django 5.2 on 2025-06-18 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoRecursoLeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('visto', 'Visto')], max_length=20)),
                ('fecha_visto', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GrupoLeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('orden', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('orden', models.IntegerField()),
                ('recurso_url', models.CharField(max_length=500)),
                ('fecha_disponible', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LeccionUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('sin ver', 'Sin ver'), ('avanzado', 'Avanzado'), ('finalizado', 'Finalizado')], max_length=20)),
                ('porcentaje_avance', models.IntegerField()),
                ('fecha_ultimo_avance', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RecursoLeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('video', 'Video'), ('imagen', 'Imagen'), ('pdf', 'PDF'), ('audio', 'Audio'), ('enlace', 'Enlace'), ('otro', 'Otro')], max_length=20)),
                ('url', models.CharField(max_length=500)),
                ('descripcion', models.TextField()),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
