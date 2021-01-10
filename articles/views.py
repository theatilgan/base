from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm,MessageForm,MessageAForm
from .models import Article,Message
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):
    if request.method == "POST":
        minPrice = request.POST["minPrice"] + "000"
        minPrice = int(minPrice)
        maxPrice = request.POST["maxPrice"] + "000"
        maxPrice= int(maxPrice)
        
        transmission = request.POST["transmission"]
        fuel = request.POST["fuel"]
        
        articles = Article.objects.filter(isSold=False)
        articles = articles.filter(price__range=(minPrice, maxPrice))
        fullPath = ""
        if transmission == "Hepsi":
            if fuel != "Hepsi":
                articles = articles.filter(fuelType=fuel)
        else:
            articles = articles.filter(transmission=transmission)
            if fuel != "Hepsi":
                articles = articles.filter(fuelType=fuel)
        carCount = len(articles)
        context = {
            "articles" : articles,
            "carCount" : carCount
        }
        return redirect("article:listCar",context)
    return render(request,"index.html")

@login_required(login_url = "user:login")
def dashboard(request):

    if request.user.is_superuser:
        articles = Article.objects.all()
        replies = Message.objects.filter(isDone=False)[:6] 
        context = {
            "articles":articles,
            "replies":replies
        }

    else:
        articles = Article.objects.filter(author=request.user)
        context = {
            "articles":articles
        }
    return render(request,"dashboard.html",context)

def listCar(request,id):
    if request.is_ajax():

        minPrice = request.POST["minPrice"] + "000"
        minPrice = int(minPrice)
        maxPrice = request.POST["maxPrice"] + "000"
        maxPrice= int(maxPrice)
        fuel = request.POST["fuel"]
        transmission = request.POST["transmission"]


        print(minPrice)
        print(maxPrice)
        print(fuel)
        print(transmission)


        articles = Article.objects.filter(isSold=False)
        articles = articles.filter(price__range=(minPrice, maxPrice))
        if transmission == "Hepsi":
            if fuel != "Hepsi":
                articles = articles.filter(fuelType=fuel)
            
        else:
            articles = articles.filter(transmission=transmission)
            if fuel != "Hepsi":
                articles = articles.filter(fuelType=fuel)
        carCount = len(articles)
        context = {
            "articles" : articles,
            "carCount" : carCount
        }
        return render(request,"includes/cartable.html",context)
    else:
        articles = Article.objects.all()
        carCount = len(articles)
        context = {
            "articles": articles,
            "carCount":carCount
        }
        return render(request,"car/list.html",context)
    
    

def detail(request,id):
    article = Article.objects.filter(id = id)
    return render(request,"car/detail.html",{"article":article})


@login_required(login_url = "user:login")
def createCar(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    context = {
        "form":form,
    }
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        return redirect("article:dashboard")
    return render(request,"car/create.html",context)

@login_required(login_url = "user:login")
def updateCar(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Araç başarıyla güncellendi")
        return redirect("article:dashboard")


    return render(request,"car/update.html",{"form":form})

def soldCar(request,id):
    article = Article.objects.filter(id = id)
    

def deleteCar(request,id):
    article = Article.objects.filter(id = id)
    article.delete()
    messages.success(request,"Araç Başarıyla Silindi")
    return redirect("article:dashboard")

def contact(request):
    form = MessageForm(request.POST or None,request.FILES or None)
    context = {
        "form":form,
    }
    if form.is_valid():
        article = form.save(commit=False)
        article.save()
        return redirect("article:index")
    return render(request,"contact/contact.html",context)

@login_required(login_url = "user:login")
def updateContact(request,id):
    uMessage = get_object_or_404(Message,id = id)
    form = MessageAForm(request.POST or None,request.FILES or None,instance = uMessage)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Ticket başarıyla güncellendi")
        return redirect("article:dashboard")
    return render(request,"contact/update.html",{"form":form})
