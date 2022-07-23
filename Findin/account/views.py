from django.shortcuts import render, redirect
from django.contrib import messages
from .form import registerform


def dashboard(request):
    return render(request, 'account/index.html')


def signupform(request):
    if request.method == 'POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}!')
            return redirect('/')
    else:
        form= registerform()
    return render(request, 'account/register.html', {'form': form})

