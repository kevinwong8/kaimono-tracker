# Generated by Django 4.2.13 on 2024-07-04 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
