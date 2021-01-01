from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "article"

urlpatterns = [
    path('', views.index, name = "index"),
    path('carlist/', views.carlist, name = "carlist"),
    path('contact/', views.contact, name = "contact"),
    path('addcar/', views.addCar, name = "addcar"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('delete/<int:id>',views.deleteCar,name = "delete"),
    path('dashboard/', views.dashboard, name = "dashboard"),

    path('cars/', views.AracListesi.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
