from django import forms

class AddUserForm(forms.Form):
    name=forms.CharField(label='Name',max_length=200)
    email=forms.EmailField(label='Email',max_length=200)
    password=forms.CharField(label='Password',max_length=200,widget=forms.PasswordInput())
class LoginUser(forms.Form):
    email=forms.EmailField(label='Email',max_length=200)
    password=forms.CharField(label='Password',max_length=200,widget=forms.PasswordInput())