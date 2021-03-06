# Generated by Django 3.1.4 on 2020-12-29 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20201229_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleimage',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='articles.article', verbose_name='Araç'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='bodyType',
            field=models.TextField(choices=[('Diğer', 'Diğer'), ('Suv', 'Suv'), ('Crossover', 'CrossOver'), ('Sedan', 'Sedan'), ('Hathcback', 'Hathcback')], verbose_name='Kasa'),
        ),
        migrations.AlterField(
            model_name='article',
            name='fuelType',
            field=models.TextField(choices=[('Benzin Lpg', 'Benzin Lpg'), ('Hybrid', 'Hybrid'), ('Elektrik', 'Elektrik'), ('Benzin', 'Benzin'), ('Dizel', 'Dizel')], verbose_name='Yakıt'),
        ),
    ]
