# Generated by Django 3.1.7 on 2021-09-08 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0004_auto_20210906_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='moto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motos.moto'),
        ),
    ]
