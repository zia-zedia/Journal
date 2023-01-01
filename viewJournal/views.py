from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from addEntry.models import JournalEntry
from addEntry.forms import PostForm
# Create your views here.

def list_view(request):
    
    latest_journal_list = JournalEntry.objects.order_by('-creationDate')
    context = {'latest_journal_list': latest_journal_list}

    return render(request, 'list_view.html',context)

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(JournalEntry, id = id)
 
    # pass the object as instance in form
    form = PostForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/posts")
    
    context["form"] = form
 
    return render(request, "update_view.html", context)
  
def delete_view(request, id):
    context ={}
    obj = get_object_or_404(JournalEntry, id = id)
 
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/posts")
 
    return render(request, "delete_view.html", context)