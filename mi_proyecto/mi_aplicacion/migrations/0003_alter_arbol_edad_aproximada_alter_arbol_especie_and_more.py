# Generated by Django 5.0.6 on 2024-11-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0002_auto_20241123_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbol',
            name='edad_aproximada',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='arbol',
            name='especie',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='arbol',
            name='imagen',
            field=models.ImageField(upload_to='arboles_imagenes/'),
        ),
        migrations.AlterField(
            model_name='arbol',
            name='latitud',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='arbol',
            name='longitud',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='arbol',
            name='nombre_cientifico',
            field=models.CharField(max_length=255),
        ),
    ]
