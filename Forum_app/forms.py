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

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['desc']

    def save(self):
        _forum = forum.objects.get(id=self.initial["forum_id"])
        return Comment.objects.create(
            forum=_forum,
            user=self.initial["user"],
            desc=self.cleaned_data["desc"]
        )
