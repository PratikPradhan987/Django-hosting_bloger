from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username Already Exist.")
            return redirect('/sign_up/')

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
        )

        messages.success(request, "Account created successfully.")
        # Render the same page to display the success message
        return render(request, 'sign_up.html')
    return render(request, 'sign_up.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            # Redirect to a success page or home page after login                            
            return redirect('/landing_page') # Adjust the redirect URL as needed
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/') # Redirect back to the login page with error message
        
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('/')  
    