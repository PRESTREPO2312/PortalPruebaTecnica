# Generated by Django 4.2.7 on 2023-11-15 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ofertasempleados', '0002_alter_usuario_apellidos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombres',
        ),
    ]
