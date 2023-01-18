from django.shortcuts import render
from basicapp.forms import user,Userinfo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def register(request):
    registered=False

    if(request.method=='POST'):

        users=user(request.POST)
        info=Userinfo(request.POST)

        if users.is_valid() and info.is_valid():
            userss=users.save()
            userss.set_password(userss.password)
            userss.save()
            useringo=info.save(commit=False)
            useringo.user=userss
            if 'picture' in request.FILES:
                useringo.picture=request.FILES['picture']
            
            useringo.save()

            registered=True
    else:
        users=user()
        info=Userinfo()
    return render(request,"basicapp/registration.html",{'users':users,'info':info,'registered':registered})


def user_login(request):
    if request.method=='POST':
        usernames=request.POST.get('username')
        passwords=request.POST.get('password')

        user=authenticate(username=usernames,password=passwords)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tries to login with incorrect username and password")
    return render(request,'basicapp/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

