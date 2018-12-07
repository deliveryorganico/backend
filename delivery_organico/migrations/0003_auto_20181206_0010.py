# Generated by Django 2.1.2 on 2018-12-06 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_organico', '0002_auto_20181205_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=60, null=True, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=15, null=True, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='locality',
            field=models.CharField(max_length=15, null=True, verbose_name='Localidad'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=30, null=True, verbose_name='Telefono'),
        ),
    ]