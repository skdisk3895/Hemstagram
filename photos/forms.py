from django import forms
from .models import Photo, Comment

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'content')
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder': '나의 이야기',
                    }
            ),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('opinion', )
        widgets = {
            'opinion': forms.TextInput(
                attrs={'placeholder': '댓글 달기',
                       'class': 'comment-input',
            }),
        }