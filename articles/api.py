from rest_framework import generics
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article
from django.contrib.auth.decorators import login_required



class ArticleApi(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class ArticleCreateApi(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class ArticleUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class ArticleDeleteApi(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

