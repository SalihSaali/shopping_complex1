from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.import views
from django.http import HttpResponse

def ab(request):
    return HttpResponse('reh')

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken")
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already taken")
            else:
               user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
               user.save()
               messages.info(request,"user created")
               return redirect('/')
        else:
            messages.info(request,"password not matched")
            return redirect('reg')

    else:
        return render(request,"registration.html")