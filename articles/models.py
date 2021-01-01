from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

FuelTypes = {
    ("Benzin","Benzin"),
    ("Benzin Lpg","Benzin Lpg"),
    ("Dizel","Dizel"),
    ("Elektrik","Elektrik"),
    ("Hybrid","Hybrid"),
}
BodyTypes = {
    ("Sedan","Sedan"),
    ("Suv","Suv"),
    ("Hathcback","Hathcback"),
    ("Crossover","CrossOver"),
    ("Diğer","Diğer"),
}
Transmission = {
    ("Otomatik","Otomatik"),
    ("Yarı Otomatik","Yarı Otomatik"),
    ("Manuel","Manuel"),
    
}


class Article(models.Model):

    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Ekleyen")
    pic = models.FileField(blank=True,null=True,verbose_name="Fotoğraf")
    year = models.PositiveIntegerField(default=2020,validators=[MaxValueValidator(2021),
            MinValueValidator(1980)],verbose_name="Yıl")
    km = models.FloatField(verbose_name="Km")
    price = models.FloatField(verbose_name="Fiyat")
    make = models.CharField(max_length = 20,verbose_name="Marka")
    model = models.CharField(max_length = 20,verbose_name="Model")
    transmission = models.TextField(choices=FuelTypes,verbose_name="Vites")
    fuelType = models.TextField(choices=FuelTypes,verbose_name="Yakıt")
    bodyType = models.TextField(choices=BodyTypes,verbose_name="Kasa")
    engine = models.CharField(blank=True,null=True,max_length = 20,verbose_name="Motor")
    variant = models.CharField(blank=True,null=True,max_length = 20,verbose_name="Paket")
    content = RichTextField(blank=True,null=True,verbose_name="Detay")
    isSold = models.BooleanField(default=False,verbose_name="Durum")

    def __str__(self):
        return self.make
    

    

    




    