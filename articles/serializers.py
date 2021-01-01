from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ('alis','satis') // belirtilen kisimlari ceker.
        # fields = '__all__' // tum kisimlari ceker.
        fields = '__all__'