from django import forms
from .models import Article,Message
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
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
            "highlighted",

        ]
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            "nameSurname",
            "replyOption",
            "phone",
            "mail",
            "subject",
        ]
class MessageAForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            
            "isDone",
            "nameSurname",
            "replyOption",
            "phone",
            "mail",
            "subject",
            "notes",

        ]