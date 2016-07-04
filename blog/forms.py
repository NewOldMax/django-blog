from django.forms import ModelForm, TextInput, Textarea
from markitup.widgets import MarkItUpWidget
from models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': '5'}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': MarkItUpWidget(attrs={'class': 'form-control', 'rows': '5'}),
        }