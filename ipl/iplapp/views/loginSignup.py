from django.views import View
from iplapp.models import *
from django.shortcuts import render,redirect
from django.urls import resolve
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.models import User

from django.contrib import messages

def logout_user(request):
    logout(request)
    return redirect('http://localhost:8000/')
from iplapp.forms.loginNSignUpForm import *

class loginPage(View):
    def get(self,request,*args,**kwargs):
        login_form=LoginForm()
        return render(
            request,
            template_name='iplapp/loginPage.html',
            context={'form':login_form}
        )
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=request.POST['userName']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('http://localhost:8000/seasons/')
            else:
                print("worng password")

class signupPage(View):
    def get(self,request,*args,**kwargs):
        signup_form=SignUpForm()
        return render(
            request,
            template_name='iplapp/signUpPage.html',
            context={'form':signup_form}

        )
    def post(self,request,*args,**kwargs):
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(**form.cleaned_data)
            user.save()
            login(request,user)
            return redirect('http://localhost:8000/login/')
