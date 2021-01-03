from rest_framework import serializers
from .models import Article
from rest_framework.validators import UniqueTogetherValidator


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ('alis','satis') // belirtilen kisimlari ceker.
        # fields = '__all__' // tum kisimlari ceker.
        fields = [
            "author",
            "pic",
            "year",
            "km",
            "price",
            "make",
            "model",
            "transmission",
            "fuelType",
            "bodyType",
            "engine",
            "variant",
            "content",
            "isSold",
        ]
        
        