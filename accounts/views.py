from django.shortcuts import redirect, render
from .forms import CustomUserFormCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def register(request):
    form = CustomUserFormCreationForm
    if request.method == 'POST':
        form = CustomUserFormCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect(login)
            messages.success(
                request, f'Hurray account was created for ' + user)
        else:  
            messages.info(
                request, f'Invalid form, ensure all fields are correct')
            
    return render(request, 'accounts/register.html', {'form':form})

def login(request):
    form = CustomAuthenticationForm()
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request)
                messages.success(
                request, f'You logged in Successfully')
                return redirect('success')
        else:
            form = CustomAuthenticationForm()    
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    return render(request, 'accounts/logout.html')

def success(request):
    return render(request, 'accounts/success.html')