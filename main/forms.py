from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import News
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100, required=True, label="ПІБ")
    phone_number = forms.CharField(max_length=15, required=True, label="НОМЕР ТЕЛЕФОНУ")
    photo = forms.ImageField(required=False, label="Завантажте своє фото")

    class Meta:
        model = User
        fields = ["username", "full_name", "phone_number", "email", "password1", "password2", "photo"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']
