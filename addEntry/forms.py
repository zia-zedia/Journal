from django import forms
from .models import JournalEntry
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class PostForm(forms.ModelForm):

    class Meta:
        model = JournalEntry
        fields = ['title','text']