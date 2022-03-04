from django.shortcuts import render,redirect
from .forms import *
from .models import *



def home(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'home.html',context)
    

def addInForum(request):
    form = CreateInForum()
    if request.method == "POST":
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'addInForum.html', context)
    
    
def addInDiscussion(request):
    form = CreationInDiscussion()
    if request.method == "POST":
        form = CreationInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'addInDiscussion.html', context)

def delete(request,id):
    forum.objects.get(pk=id).delete()
    return redirect('home')
    
    	
      


    
    

