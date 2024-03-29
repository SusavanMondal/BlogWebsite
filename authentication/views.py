from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def authlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['Password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password!!!')

    return render(request, 'authentication/login.html')
def authlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')

def authforgetpassword(request):
    return render(request, 'authentication/forgetpass.html')
def authregistration(request):

    if request.method == 'POST':
        username=request.POST['Name']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        Email=request.POST['Email']
        mobile_number=request.POST['mobile_number']
        if confirm_password==password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "USername already exists")
            elif User.objects.filter(email=Email).exists():
                messages.error(request, "Email already exists")
            else:
                user=User.objects.create_user(username=username, password=password, email=Email)
                user.save()
                return redirect('profile')


        else:
            messages.error(request, "password and confirm_password does not match")


        



    return render(request, 'authentication/registration.html')
