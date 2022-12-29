from django.shortcuts import render
from .models import JournalEntry
# Create your views here.

def index(request):
    latest_journal_list = JournalEntry.objects.order_by('-creationDate')

    context = {'latest_journal_list': latest_journal_list}
    return render(request, 'index.html', context)
