from django import forms
from feeds.models import Articles


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = [
            'title',
            'post',
            'image',
            'user',
        ]
