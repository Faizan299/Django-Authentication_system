from django.forms import ModelForm
from .models import *
from django import forms

class CreateInForum(ModelForm):
    class Meta:
        model = forum
        fields = "__all__"
        
class CreationInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"

class CommentForm(forms.Form):
    desc = forms.CharField(widget=forms.Textarea)