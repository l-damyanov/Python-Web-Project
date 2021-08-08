from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


UserModel = get_user_model()


class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# class SignInForm(forms.Form):
#
#     def __init__(self, *args, **kwargs):
#         super(SignInForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#
#     user = None
#     email = forms.EmailField()
#     password = forms.CharField(
#         widget=forms.PasswordInput(),
#     )
#
#     def clean_password(self):
#         self.user = authenticate(
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password'],
#         )
#
#         if not self.user:
#             raise ValidationError('Email and/or password is incorrect!')
#
#     def save(self):
#         return self.user


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserModel
        fields = ('email',)
