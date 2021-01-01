from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm,MessageForm
from .models import Article,Message
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializer

# Create your views here.

def index(request):
    return render(request,"index.html")

def carlist(request):
    articles = Article.objects.all()
    return render(request,"carlist.html",{"articles":articles})

def contact(request):
    form = MessageForm(request.POST or None,request.FILES or None)
    context = {
        "form":form,
    }
    if form.is_valid():
        article = form.save(commit=False)
        article.save()

        return redirect("article:index")
    return render(request,"contact.html",context)

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.all()
    replies = Message.objects.all() 
    context = {
        "articles":articles,
        "replies":replies
    }
    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addCar(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    context = {
        "form":form,
    }
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        return redirect("article:dashboard")
    return render(request,"addcar.html",context)

def detail(request,id):
    article = Article.objects.filter(id = id)
    return render(request,"detail.html",{"article":article})

def soldCar(request,id):
    article = Article.objects.filter(id = id)
    

def deleteCar(request,id):
    article = Article.objects.filter(id = id)

    article.delete()

    messages.success(request,"Makale Başarıyla Silindi")

    return redirect("article:dashboard")
    

# API 
class AracListesi(APIView):
    def get(self, request):
            araclar = Article.objects.all()
            serializer = ArticleSerializer(araclar, many=True)
            return  Response(serializer.data)
    def post(self,request):
        print("###############################")
        print("PoST")
        print("###############################")