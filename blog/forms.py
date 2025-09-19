from .models import CollaborateRequest, Comment
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)