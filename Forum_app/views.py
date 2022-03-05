from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

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
            return redirect('/home/')
    context = {'form':form}
    return render(request, 'addInForum.html', context)
    
    
def addInDiscussion(request):
    form = CreationInDiscussion()
    if request.method == "POST":
        form = CreationInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    context = {'form':form}
    return render(request, 'addInDiscussion.html', context)

def delete(request,id):
    forum.objects.get(pk=id).delete()
    return redirect('home')

def get(request,id):
    Forum = forum.objects.get(pk=id)
    comment = Comment.objects.filter(forum=Forum)
    context = {
        'forum':Forum,
        'comments':comment,
        'form_comment':CommentForm
        }
    return render(request, 'forum_detail.html', context)

class ForumListView(ListView):
    model = forum
    queryset = forum.objects.order_by('date_created')
    

def commentadd(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, initial={"forum_id": request.POST.get("forum_id"), "user": request.user})
        if form.is_valid():
            form.save()
            return redirect(reverse("getById", args=[request.POST.get("forum_id")]))
    context = {'form':form}
    return render(request, 'forum_detail.html', context)


    
    	
      


    
    

