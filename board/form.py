from django import forms
from django.contrib.auth.models import User
from board.models import Board, Task

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label="Password")
	

class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label="Password")
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label="Confirm Password")
	class Meta:
		model = User
		fields = ['username', 'email', 'password',]


class AddBoard(forms.ModelForm):
	class Meta:
		model = Board	
		fields = ['name']	




