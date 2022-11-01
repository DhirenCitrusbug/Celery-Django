from django.shortcuts import redirect, render
from django.views import View
from celery_app.forms import LoginForm
from django.contrib.auth import authenticate,login
from . tasks import *
from datetime import datetime, timedelta
from pytz import timezone,utc
# Create your views here.

class Login(View):
    def get(self,request):
        form = LoginForm()
        print(datetime.now(),'--',datetime.now()+timedelta(seconds=20))
        return render(request,'login.html',{'form':form})
    def post(self,request):
        form = LoginForm(request.POST)


        # login_mail(
        #     'Subject here',
        #     'Here is the message.',
        #     'from@example.com',
        #     ['to@example.com'],
        # )
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                # login_mail.apply_async(kwargs={'subject':'Subject here','message':'Here is the message.','from_email':'from@example.com','recipient_list':['to@example.com']})
                # login_mail.s('NEW Subject here','Here is the NEW message.','from@example.com',['to@example.com']).apply_async(countdown=20)
                # local = timezone("America/Los_Angeles")
                # naive = datetime.strptime("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
                # local_dt = local.localize(naive, is_dst=None)
                # utc_dt = local_dt.astimezone(utc)
                # utc_dt
                # print(utc_dt.strftime("%Y-%m-%d %H:%M:%S"))
                login_mail.apply_async(['NEW Subject here','Here is the NEW message.','from@example.com',['to@example.com']],eta=datetime.now()+timedelta(seconds=20))
                login(request, user)
                print(datetime.now(),'Time')
                return redirect('/admin/')
            else:
                print(form.cleaned_data)
                return render(request,'login.html',{'form':form})
        else:
            print(form['username'].errors,'error')
            return render(request,'login.html',{'form':form})
