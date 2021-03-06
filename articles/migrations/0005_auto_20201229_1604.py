# Generated by Django 3.1.4 on 2020-12-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20201229_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='bodyType',
            field=models.TextField(choices=[('Suv', 'Suv'), ('Crossover', 'CrossOver'), ('Hathcback', 'Hathcback'), ('Sedan', 'Sedan'), ('Diğer', 'Diğer')], verbose_name='Kasa'),
        ),
        migrations.AlterField(
            model_name='article',
            name='fuelType',
            field=models.TextField(choices=[('Elektrik', 'Elektrik'), ('Benzin', 'Benzin'), ('Benzin Lpg', 'Benzin Lpg'), ('Hybrid', 'Hybrid'), ('Dizel', 'Dizel')], verbose_name='Yakıt'),
        ),
    ]
