# Generated by Django 5.0.7 on 2024-09-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('serial_number', models.CharField(max_length=20)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
