# Generated by Django 2.2.6 on 2019-10-09 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppEstablecimiento', '0001_initial'),
        ('AppProfesor', '0001_initial'),
        ('AppCarrera', '0001_initial'),
        ('AppAlumno', '0001_initial'),
        ('AppCurso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClsNota',
            fields=[
                ('pk_nota', models.AutoField(primary_key=True, serialize=False)),
                ('parcial_1', models.IntegerField()),
                ('parcial_2', models.IntegerField()),
                ('zona', models.IntegerField()),
                ('parcial_3', models.IntegerField()),
                ('final', models.IntegerField()),
                ('fecha_ingreso', models.DateField()),
                ('fecha_modificacion', models.DateField()),
                ('fk_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppAlumno.ClsAlumno')),
                ('fk_carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCarrera.ClsCarrera')),
                ('fk_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCurso.ClsCurso')),
                ('fk_establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppEstablecimiento.ClsEstablecimiento')),
                ('fk_profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProfesor.ClsProfesor')),
            ],
        ),
    ]
