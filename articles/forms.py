from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "pic",
            "year",
            "km",
            "price",
            "make",
            "model",
            "fuelType",
            "bodyType",
            "engine",
            "variant",
            "content",
            "isSold",

        ]
