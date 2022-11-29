from django.shortcuts import render, redirect

from users import forms


def registration_view(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('login')
    else:
        form = forms.RegistrationForm()

    return render(request, 'users/registration.html', {'form': form})

