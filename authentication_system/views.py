from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import views as django_views
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm


class _CustomPasswordResetView(django_views.PasswordResetView):
    template_name = 'reset_password_form.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password-reset-done')
    form_class = CustomPasswordResetForm
    

class _CustomPasswordResetConfirmView(django_views.PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password-reset-complete')


class _CustomPasswordResetCompleteView(django_views.PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


class _CustomPasswordResetDoneView(django_views.PasswordResetDoneView):
    template_name = 'password_reset_done.html'


# Make views sane again

_password_reset_view = _CustomPasswordResetView.as_view()
custom_password_reset_confirm = _CustomPasswordResetConfirmView.as_view()
custom_password_reset_complete = _CustomPasswordResetCompleteView.as_view()
custom_password_reset_done = _CustomPasswordResetDoneView.as_view()

    


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
            return render(request,'welcome.html',context)
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

def custom_password_reset(request):
    if request.method == "POST" and request.is_limited():
        return redirect(reverse("password-reset"))

    return _password_reset_view(request)
    