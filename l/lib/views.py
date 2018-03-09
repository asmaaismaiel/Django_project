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

def register(request):
    if request.method=='POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            try:
                user=User.objects.get(email=form.cleaned_data['email'])
                return HttpResponse('your email exists')
            except User.DoesNotExist:
                user=User()
                user.name=form.cleaned_data['name']
                user.email=form.cleaned_data['email']
                user.password = form.cleaned_data['password']
                user.save()
                return redirect ('login')
    else:
        form = AddUserForm()
        return render(request,'lib/register.html',{'form':form})
def home(request):
    if 'member_name' in request.session and request.session['member_name']:
        data=Auther.objects.all()
        return render (request ,'lib/home.html',{'name':request.session['member_name'],'data':data})
    else:
        form=LoginUser()
        return render (request,'lib/login.html',{'form':form})
         
def viewAuthor(request):
    if 'member_name' in request.session and request.session['member_name']:
        author=Auther.objects.get(aid=request.GET.get('author_id',''))
        books=Book.objects.filter(auther_id=author.aid)
        return render(request,'lib/single.html',{'name':request.session['member_name'],'author':author,'books':books})
    else:
        form = AddUserForm()
        return render(request,'lib/register.html',{'form':form})
def viewBook(request):
    if 'member_name' in request.session and request.session['member_name']:
        book=Book.objects.get(bid=request.GET.get('book_id',''))
        return render(request,'lib/book.html',{'name':request.session['member_name'],'book':book,'author':book.auther_id})
    else:
        form = AddUserForm()
        return render(request,'lib/register.html',{'form':form})
def viewAbout(request):
    return render(request,'lib/about.html')
def logout(request):
    request.session.clear()
    return redirect('login')
