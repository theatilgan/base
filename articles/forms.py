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
            "fuelType",
            "bodyType",
            "engine",
            "variant",
            "content",
            "isSold",

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