# Generated by Django 3.2.20 on 2023-08-27 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_alter_libro_librocategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='libroCategoria',
            field=models.CharField(choices=[('ficcion', 'Ficcion'), ('ciencias', 'Ciencias'), ('infantil', 'Infantil'), ('otro', 'Otro')], default='ficcion', max_length=15),
        ),
    ]
