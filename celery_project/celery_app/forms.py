from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True,'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control'}),
    )
# class LoginForm(forms.ModelForm):

#     class Meta:
#         username = forms.TextInput()
#         model = User

#         fields = ['username','password']

#         widgets = {
#             'username':forms.TextInput(attrs={'class':'form-control'}),
#             'password':forms.PasswordInput(attrs={'class':'form-control'}),
#     }