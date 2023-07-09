from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.

def register(request):
    # check if there is post method or not 
    if request.method == 'POST':
        # checking validation of form
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been created')
            return redirect('food:index')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

