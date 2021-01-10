from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .api import  ArticleApi,ArticleCreateApi,ArticleUpdateApi,ArticleDeleteApi

app_name = "article"

urlpatterns = [
    path('', views.index, name = "index"),
    path('dashboard/', views.dashboard, name = "dashboard"),

    path('list/<str:id>', views.listCar, name = "listCar"),
    path('car/<int:id>',views.detail,name = "detail"),
    path('create/', views.createCar, name = "createCar"),
    path('update/<int:id>',views.updateCar,name = "update"),
    path('delete/<int:id>',views.deleteCar,name = "delete"),
    
    path('contact/', views.contact, name = "contact"),
    path('contact/<int:id>', views.updateContact, name = "updateContact"),

    # API
    path('api/',ArticleApi.as_view()),
    path('api/create',ArticleCreateApi.as_view()),
    path('api/<int:pk>',ArticleUpdateApi.as_view()),
    path('api/<int:pk>/delete',ArticleDeleteApi.as_view()),


    
]
urlpatterns = format_suffix_patterns(urlpatterns)
