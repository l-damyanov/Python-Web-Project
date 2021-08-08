from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from rent_a_house.rent_a_house_auth.forms import SignInForm, SignUpForm


class SignInView(LoginView):
    template_name = 'sign_in.html'
    authentication_form = SignInForm

    def get_success_url(self):
        return reverse('profile page')

# def sign_in(req):
#     if req.method == 'POST':
#         form = SignInForm(req.POST)
#         if form.is_valid():
#             user = form.save()
#             login(req, user)
#             return redirect('profile page')
#     else:
#         form = SignInForm()
#     context = {
#         'form': form,
#     }
#     return render(req, 'sign_in.html', context)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'sign_up.html'

    def get_success_url(self):
        return reverse('profile page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

# def sign_up(req):
#     if req.method == 'POST':
#         form = SignUpForm(req.POST, req.FILES)
#         if form.is_valid():
#             user = form.save()
#             login(req, user)
#             return redirect('profile page')
#     else:
#         form = SignUpForm()
#     context = {
#         'form': form,
#     }
#     return render(req, 'sign_up.html', context)


def sign_out(req):
    logout(req)
    return redirect('home page')
