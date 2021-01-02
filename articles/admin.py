from django.contrib import admin
from .models import Article,Message
# Register your models here.



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["author","make","model","price"]

    list_display_links = ["author","make","model","price"]

    search_fields = ["author","make","model","price"]

    list_filter = ["isSold","date"]
    class Meta:
        model = Article

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ["nameSurname","isDone","date"]

    list_display_links = ["nameSurname","isDone","date"]

    search_fields = ["nameSurname","isDone","date"]

    list_filter = ["isDone","date"]
    class Meta:
        model = Article
