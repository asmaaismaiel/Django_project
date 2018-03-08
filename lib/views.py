from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from lib.models import *
# Create your views here.
def login(request):
    if 'member_name' in request.session and request.session['member_name']:
        return redirect('home')
    else:
        if request.method=='POST':
            form=LoginUser(request.POST)
            if form.is_valid():
                try:
                    user=User.objects.get(email=form.cleaned_data['email'])
                    if user.password == form.cleaned_data['password']:
                        request.session['member_name']=user.name
                        return redirect('home')
                    else:
                        return HttpResponse('please check your password')
                except User.DoesNotExist:
                    return redirect('login')
        else:
            form=LoginUser()
            return render (request,'lib/login.html',{'form':form})
def logout(request):
    request.session.clear()
    return redirect('login')
