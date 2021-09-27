# Generated by Django 3.1.7 on 2021-09-07 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0003_alter_moto_modelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mantenimientos',
            name='id_historial',
        ),
        migrations.AddField(
            model_name='mantenimientos',
            name='moto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='motos.moto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mantenimientos',
            name='responsable',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='motos.persona'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historial',
            name='estado',
            field=models.CharField(choices=[('Vendida', 'Vendida'), ('Rechazada', 'Rechazada'), ('Pendiente', 'Pendiente'), ('En propiedad', 'En propiedad')], default='En propiedad', max_length=20),
        ),
        migrations.AlterField(
            model_name='historial',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mantenimientos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='moto',
            name='foto_moto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_motos'),
        ),
        migrations.AlterField(
            model_name='moto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]