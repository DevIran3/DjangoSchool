# Generated by Django 2.2.6 on 2019-10-09 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppCarrera', '0001_initial'),
        ('AppUsuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClsAlumno',
            fields=[
                ('pk_alumno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('fecha_ingreso', models.DateField()),
                ('contacto', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=100)),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.IntegerField()),
                ('fk_carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCarrera.ClsCarrera')),
                ('fk_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUsuario.ClsUsuario')),
            ],
        ),
    ]
