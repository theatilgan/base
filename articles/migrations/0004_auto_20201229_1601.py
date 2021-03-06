# Generated by Django 3.1.4 on 2020-12-29 13:01

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0003_remove_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Cc',
            field=models.PositiveIntegerField(default=1, verbose_name='Cc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Ekleyen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='bodyType',
            field=models.TextField(choices=[('Crossover', 'CrossOver'), ('Diğer', 'Diğer'), ('Hathcback', 'Hathcback'), ('Suv', 'Suv'), ('Sedan', 'Sedan')], default=1, verbose_name='Kasa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Detay'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='damage',
            field=models.FloatField(default=1, verbose_name='Hasar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Eklenme Tarihi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='engine',
            field=models.TextField(default=(1,), verbose_name='Motor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='fuelType',
            field=models.TextField(choices=[('Dizel', 'Dizel'), ('Benzin Lpg', 'Benzin Lpg'), ('Hybrid', 'Hybrid'), ('Benzin', 'Benzin'), ('Elektrik', 'Elektrik')], default=1, verbose_name='Yakıt'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='hPower',
            field=models.PositiveIntegerField(default=1, verbose_name='Beygir Gücü'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='isSold',
            field=models.BooleanField(default=False, verbose_name='Durum'),
        ),
        migrations.AddField(
            model_name='article',
            name='km',
            field=models.FloatField(default=1, verbose_name='Km'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='make',
            field=models.TextField(default=1, verbose_name='Marka'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='model',
            field=models.TextField(default=1, verbose_name='Model'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='plate',
            field=models.TextField(default=1, verbose_name='Plaka'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.FloatField(default=1, verbose_name='Fiyat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='variant',
            field=models.TextField(default=1, verbose_name='Paket'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.PositiveIntegerField(default=1, verbose_name='Yıl'),
            preserve_default=False,
        ),
    ]
