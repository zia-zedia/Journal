from django import forms
from .models import JournalEntry

class PostForm(forms.ModelForm):

    class Meta:
        model = JournalEntry
        fields = ('title','text')