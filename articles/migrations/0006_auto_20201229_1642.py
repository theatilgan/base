# Generated by Django 3.1.4 on 2020-12-29 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20201229_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='bodyType',
            field=models.TextField(choices=[('Suv', 'Suv'), ('Diğer', 'Diğer'), ('Hathcback', 'Hathcback'), ('Sedan', 'Sedan'), ('Crossover', 'CrossOver')], verbose_name='Kasa'),
        ),
        migrations.AlterField(
            model_name='article',
            name='engine',
            field=models.CharField(max_length=20, verbose_name='Motor'),
        ),
        migrations.AlterField(
            model_name='article',
            name='fuelType',
            field=models.TextField(choices=[('Benzin Lpg', 'Benzin Lpg'), ('Elektrik', 'Elektrik'), ('Benzin', 'Benzin'), ('Hybrid', 'Hybrid'), ('Dizel', 'Dizel')], verbose_name='Yakıt'),
        ),
        migrations.AlterField(
            model_name='article',
            name='make',
            field=models.CharField(max_length=20, verbose_name='Marka'),
        ),
        migrations.AlterField(
            model_name='article',
            name='model',
            field=models.CharField(max_length=20, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='article',
            name='plate',
            field=models.CharField(max_length=6, verbose_name='Plaka'),
        ),
        migrations.AlterField(
            model_name='article',
            name='variant',
            field=models.CharField(max_length=20, verbose_name='Paket'),
        ),
    ]
