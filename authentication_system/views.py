from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth



def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['email'])
                return render (request,'register.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['email'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('register')
        else:
            return render (request,'register.html', {'error':'Password does not match!'})
    else:
        return render(request,'register.html')
    

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            context ={
                'data':user
            }
            return render(request,'home.html',context)
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')


def logout(request):
    if not request.user.is_authenticated:
        return redirect(request.GET.get('next', reverse('login')))

    if request.method == 'POST':
         auth.logout(request)
    return render(request, 'logout.html')

