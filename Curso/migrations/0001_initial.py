# Generated by Django 2.2.7 on 2020-10-16 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre del Curso')),
                ('nota_minima', models.IntegerField(default=60, verbose_name='Nota Mínima')),
                ('sueldo', models.IntegerField(verbose_name='Pago del curso')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.CharField(help_text='Ingrese el año sin espacios, ejemplo: 2020', max_length=4, verbose_name='Ciclo de estudio')),
                ('nombre_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curso.Curso')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personal.Profesor')),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignaciones',
                'ordering': ['nombre_curso'],
            },
        ),
    ]