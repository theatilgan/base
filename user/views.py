from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout



# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)
        if User.objects.filter(username=username).exists():
            messages.info(request,"Bu kullanıcı adı alınmış...")
        else:
            newUser.save()
            login(request,newUser)
            messages.info(request,"Başarıyla Kayıt Oldunuz...")
            return redirect("article:index")
    context = {
            "form":form
        }
    return render(request,"user/register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("article:index")
    return render(request,"user/login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("article:index")

