from django import forms
class LoginUser(forms.Form):
    email=forms.EmailField(label='Email',max_length=200)
    password=forms.CharField(label='Password',max_length=200,widget=forms.PasswordInput())
