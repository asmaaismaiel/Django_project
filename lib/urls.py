from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('register/',views.register,name='register'),
    path('viewAuthor/',views.viewAuthor,name='viewAuthor'),
    path('home/',views.home,name='home'),
    path('viewAbout/',views.viewAbout,name='viewAbout'),
    path('logout/',views.logout,name='logout'),
]
