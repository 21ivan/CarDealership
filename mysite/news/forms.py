from django import forms
from news.models import Articles


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = [
            'title',
            'post',
            'image',
            'user',
        ]
