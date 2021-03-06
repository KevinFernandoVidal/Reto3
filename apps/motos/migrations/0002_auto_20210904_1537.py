# Generated by Django 3.2.6 on 2021-09-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moto',
            name='cilindraje',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='moto',
            name='modelo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
