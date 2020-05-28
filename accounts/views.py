from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accounts.forms import UserForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            messages.success(request, 'Successfully registered, Please login to continue')
            return redirect('login')
        else:
            messages.error(request, 'Invalid! Please try again')
            return redirect('register')

    user_form = UserForm()
    context = {
        'form' : user_form
    }
    return render(request, 'accounts/register.html', context)







    # if request.method == 'POST':
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # password1 = request.POST['password2']
        # form = UserForm(data=request.POST)
        # if password == password1:
        #     if User.objects.filter(username=username).exists():
        #         messages.error(request, "Username already exists")
        #         return redirect('register')
        #     else:
        #         if User.objects.filter(email=email).exists():
        #             messages.error(request, 'Email already registered')
        #             return redirect('register')
        #         else:
        #             messages.success(request, 'Successfuly registered, login to continue')
        #             form = form.save()
        #             return redirect('login')
        # else:
        #     return redirect('register')
    # form = UserForm()
    # context = {
    #     'form':form,
    # }
    # return render(request, 'accounts/register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            # Success message that you're logged in
            login(request, user)
            return redirect('dashboard')
            # Show logout button
            # Login user and show personlized stuff here
        else:
            # Show validation error
            return redirect('login')

    return render(request, 'accounts/login.html')
    
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')
