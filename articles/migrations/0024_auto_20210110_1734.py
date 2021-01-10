# Generated by Django 3.1.4 on 2021-01-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0023_auto_20210103_1559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='article',
            name='bodyType',
            field=models.TextField(choices=[('Sedan', 'Sedan'), ('Hathcback', 'Hathcback'), ('Crossover', 'CrossOver'), ('Diğer', 'Diğer'), ('Suv', 'Suv')], verbose_name='Kasa'),
        ),
        migrations.AlterField(
            model_name='article',
            name='fuelType',
            field=models.TextField(choices=[('Benzin', 'Benzin'), ('Benzin Lpg', 'Benzin Lpg'), ('Hybrid', 'Hybrid'), ('Dizel', 'Dizel'), ('Elektrik', 'Elektrik')], verbose_name='Yakıt'),
        ),
        migrations.AlterField(
            model_name='article',
            name='km',
            field=models.PositiveIntegerField(verbose_name='Km'),
        ),
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='article',
            name='transmission',
            field=models.TextField(choices=[('Otomatik', 'Otomatik'), ('Yarı Otomatik', 'Yarı Otomatik'), ('Manuel', 'Manuel')], verbose_name='Vites'),
        ),
        migrations.AlterField(
            model_name='message',
            name='replyOption',
            field=models.TextField(blank=True, choices=[('Mail', 'Mail'), ('Telefon', 'Telefon')], null=True, verbose_name='Nasıl dönüş yapalım'),
        ),
    ]
