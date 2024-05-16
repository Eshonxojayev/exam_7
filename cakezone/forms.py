from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(RegisterForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['email'].required = True
        self.fields['first_name'].required = True

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password', min_length=8, max_length=32)
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Repeat Your Password', min_length=8, max_length=32)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Password didn't match")
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email already exists")
        return data

    # class RegisterForm(UserCreationForm):
#
#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)
#         self.fields['email'].help_text = None
#         self.fields['first_name'].help_text = None
#     #
#     # class Meta:
#     #     model = User
#     #     fields = ('username', 'email', '<PASSWORD>', '<PASSWORD>')
#
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password1'] != cd['password2']:
#             raise forms.ValidationError("Passwords don't match")
#         return cd['password2']
#
#     def clean_email(self):
#         data = self.cleaned_data['email']
#         if User.objects.filter(email=data).exists():
#             raise forms.ValidationError("Email already registered")
#         return data
