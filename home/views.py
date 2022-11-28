from django.shortcuts import render, redirect

from . import forms


def home(request):
    return render(request, 'home/home.html')


def contact_message_view(request):
    form = forms.ContactMessageForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home:home')

    return render(request, 'home/contact_message.html', {'form': form})
