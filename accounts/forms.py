from django import forms
from django.contrib.auth import get_user_model
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30 , widget=forms.PasswordInput)    
    captcha = CaptchaField()
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

class Change_passwordForm(forms.Form):
    old_pass = forms.CharField(max_length=25, widget=forms.PasswordInput)
    new_pass1 = forms.CharField(max_length=30, widget= forms.PasswordInput)
    new_pass2 = forms.CharField(max_length=30, widget= forms.PasswordInput)

class ResetPassForm(forms.Form):
    email = forms.EmailField()

class ResetPassComfirm(forms.Form):
    new_pass1 = forms.CharField(max_length=30, widget= forms.PasswordInput)
    new_pass2 = forms.CharField(max_length=30, widget= forms.PasswordInput)

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name' , 'last_name', 'id_coad' , 'phone' , 'image']