from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User




# Create your views here.
def register(request):
    if request.method== 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 !=pass2:
            return HttpResponse('your password are not the same')
        else:
            myuser = User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect('users-login')
    return render(request, 'users/register.html')

def user_login(request):
    if request.method== 'POST':
        uname = request.POST['username']
        pass1= request.POST['password']
        user = authenticate(request,username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('topic')
        else:
            return HttpResponse('incorrect username and password!!')
    return render(request, 'users/login.html')
