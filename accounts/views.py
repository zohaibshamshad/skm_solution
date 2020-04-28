from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password2']

        if password == password1:
            if User.objects.filter(username=username).exists():
                # Show them error that username is taken
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    #Show error messaga that already registered
                    return redirect('register')
                else:
                    # Everython looks good
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    return redirect('login')
        else:
            return redirect('register')
        
    return render(request, 'accounts/register.html')

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
