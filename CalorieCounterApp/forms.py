from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="",widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Username'
        }
    ))
    email = forms.EmailField(label="",widget=forms.EmailInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Email'
        }
    ))
    password1 = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Password'
        }
    ))
    password2 = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Confirm Password'
        }
    ))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="",widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Username'
        }
    ))
    password = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Password'
        }
    ))

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Old Password'
        }
    ))
    new_password1 = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input New Password'
        }
    ))
    new_password2 = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Confirm Password'
        }
    ))

class UserProfileForm(forms.ModelForm):
    name = forms.CharField(label="",widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Name'
        }
    ))
    age = forms.IntegerField(label="",widget=forms.NumberInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Age'
        }
    ))
    gender = forms.ChoiceField(label="",choices=[('', 'Select Gender'), ('Male', 'Male'), ('Female', 'Female')],widget=forms.Select(
        attrs={
            'class' : 'form-control',
        }
    ))
    height = forms.FloatField(label="",widget=forms.NumberInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Height'
        }
    ))
    weight = forms.FloatField(label="",widget=forms.NumberInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Weight'
        }
    ))
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'gender', 'height', 'weight']

class ConsumedCalorieForm(forms.ModelForm):
    item_name = forms.CharField(label="",widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Item Name'
        }
    ))
    calorie_consumed = forms.FloatField(label="",widget=forms.NumberInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Calories'
        }
    ))
    class Meta:
        model = ConsumedCalorie
        fields = ['item_name', 'calorie_consumed']