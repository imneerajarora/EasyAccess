import random
from django.core.mail import send_mail
from .forms  import RegisterForm  , LoginForm
from django.contrib.auth import authenticate , login , logout 
from django.shortcuts import render , redirect, HttpResponse , get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import UserOTP
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  #keep the account inactive untill the verified
            user.save()

            otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=user,otp=otp)

            subject = 'Your Account Verification OTP'
            message = f'Your OTP is {otp}. Use this to verify your account.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, email_from, recipient_list)

            messages.success(request,'Account Created! Please verify your email to activate the account.')
            return redirect('verify_otp',user_id = user.id)
    else:
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})



def verify_otp(request,user_id):
    user = get_object_or_404(User , id=user_id)

    if request.method == 'POST':
        otp = request.POST.get('otp')
        if UserOTP.objects.filter(user=user , otp=otp).exists():
            user.is_active = True
            user.save()
            UserOTP.objects.filter(user=user).delete()
            messages.success(request,'Account verified successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid OTP.please try again.')
    return render(request,'registration/verify_otp.html',{'user':user})



def loginview(request):
    nexturl = request.GET.get('next','/')
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        # print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate( username = username, password = password)
            if user is not None:
                if user.is_active:
                   login(request,user)
                   return HttpResponseRedirect(nexturl)
                else:
                    form.add_error(None,"Your account is inactive.please contact support or activate your account.")
            # else:
            #     # form.add_error(None,"Invalid username or password")
            #     print(form.errors)
    else:
        form = LoginForm()
    return render(request,'registration/loginpg.html',{'form':form})



@login_required
def logoutview(request):
    logout(request)
    return redirect('home')
        
            


