from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create signup View.
def sign_up(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created successfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'app/sign_up.html', {'form': fm})

# Create login View.
def log_in(request):
    if not request.user.is_authenticated:

        if request.method=='POST':
            fm = AuthenticationForm(request=request, data=request.POST) # match credentials from data base
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user = authenticate(username = uname, password= upass)

                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successfully !!!')
                    return HttpResponseRedirect('/user_profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'app/log_in.html', {'form':fm})
    else:
        return HttpResponseRedirect('/user_profile/')

# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'app/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/log_in/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/log_in/')

