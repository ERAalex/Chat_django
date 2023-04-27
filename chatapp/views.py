from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login

def frontpage(request):
    return render(request, 'chatapp/frontpage.html')


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('frontpage')

    else:
        form = SignUpForm()

    return render(request, 'chatapp/signup.html', {'form': form})