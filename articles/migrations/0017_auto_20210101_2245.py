# Generated by Django 3.1.4 on 2021-01-01 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20210101_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='bodyType',
            field=models.TextField(choices=[('Hathcback', 'Hathcback'), ('Diğer', 'Diğer'), ('Suv', 'Suv'), ('Crossover', 'CrossOver'), ('Sedan', 'Sedan')], verbose_name='Kasa'),
        ),
        migrations.AlterField(
            model_name='article',
            name='fuelType',
            field=models.TextField(choices=[('Dizel', 'Dizel'), ('Elektrik', 'Elektrik'), ('Benzin Lpg', 'Benzin Lpg'), ('Benzin', 'Benzin'), ('Hybrid', 'Hybrid')], verbose_name='Yakıt'),
        ),
        migrations.AlterField(
            model_name='article',
            name='transmission',
            field=models.TextField(choices=[('Dizel', 'Dizel'), ('Elektrik', 'Elektrik'), ('Benzin Lpg', 'Benzin Lpg'), ('Benzin', 'Benzin'), ('Hybrid', 'Hybrid')], verbose_name='Vites'),
        ),
    ]