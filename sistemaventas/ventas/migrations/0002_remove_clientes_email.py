# Generated by Django 5.1.2 on 2024-11-18 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='email',
        ),
    ]
