# Generated by Django 4.2.6 on 2023-11-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camaras', '0005_alter_camara_angulo_de_vision_alter_camara_precio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='camara',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='camaras/'),
        ),
    ]
