# Generated by Django 4.2.13 on 2024-07-06 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_barang_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barang',
            name='user',
        ),
    ]