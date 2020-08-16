from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully register the user.")
    else:
        form = SignupForm()
    context ={'form': form}
    return render(request, "account/signup.html", context)

def login(request):
    if request.method=="POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if request.POST['next']:
                return redirect(request.POST['next'])
            else:
                return redirect('home')
        else:
            return render(request, 'account/login.html', {"error":"Someting Wrong! try again."})
    return render(request, "account/login.html")
    
 
@login_required(login_url='/account/login/')
def logout(request):
    if request.method=="GET":
        auth.logout(request)
        messages.info(request, "Successfully Logout.")
        return redirect('home')