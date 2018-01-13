from django import forms
from .models import Institucion, Turno, Visitante 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import app_turnos

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20, widget = forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','password')