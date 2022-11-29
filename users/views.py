from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users import forms


def registration_view(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('users:login_view')
    else:
        form = forms.RegistrationForm()

    return render(request, 'users/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:home')
    else:
        form = forms.LoginForm(request)

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('users:login_view')
