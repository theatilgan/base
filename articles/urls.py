from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .api import  ArticleApi,ArticleCreateApi,ArticleUpdateApi,ArticleDeleteApi

app_name = "article"

urlpatterns = [
    path('', views.index, name = "index"),
    path('carlist/', views.carlist, name = "carlist"),
    path('contact/', views.contact, name = "contact"),
    path('addcar/', views.addCar, name = "addcar"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('delete/<int:id>',views.deleteCar,name = "delete"),
    path('dashboard/', views.dashboard, name = "dashboard"),

    # API
    path('api/',ArticleApi.as_view()),
    path('api/create',ArticleCreateApi.as_view()),
    path('api/<int:pk>',ArticleUpdateApi.as_view()),
    path('api/<int:pk>/delete',ArticleDeleteApi.as_view()),


    
]
urlpatterns = format_suffix_patterns(urlpatterns)
