from django import forms
from .models import Photo, Comment

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'content', 'image', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('opinion', )