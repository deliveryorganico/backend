# Generated by Django 2.1.2 on 2018-12-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_organico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='img/default_product.jpg', upload_to='img/', verbose_name='Foto'),
        ),
    ]
