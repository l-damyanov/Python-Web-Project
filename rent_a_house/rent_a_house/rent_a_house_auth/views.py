from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from rent_a_house.rent_a_house_auth.forms import SignInForm, SignUpForm


def sign_in(req):
    if req.method == 'POST':
        form = SignInForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('profile page')
    else:
        form = SignInForm()
    context = {
        'form': form,
    }
    return render(req, 'sign_in.html', context)


def sign_up(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST, req.FILES)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('profile page')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(req, 'sign_up.html', context)


def sign_out(req):
    logout(req)
    return redirect('home page')
