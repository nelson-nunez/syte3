from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
