# Generated by Django 5.0.7 on 2024-09-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traking_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
