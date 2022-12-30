from django.shortcuts import render
from datetime import datetime
from .models import JournalEntry
from .forms import PostForm
# Create your views here.

def index(request):
    
    form = PostForm()
    context = {'form':form}

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            creationDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            entryObj = JournalEntry(title = title, text = text,creationDate = creationDate)
            entryObj.save()

    return render(request, 'index.html', context)
