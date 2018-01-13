from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import Http404
from django.contrib.auth.models import User
from .models import Institucion, Visitante, Turno

#-------------------------------------------------------
from django.conf import settings
from io import BytesIO
# from reportlab.pdfgen import canvas
from django.views.generic import View
from django.http import HttpResponse

from django.views.generic import ListView
# from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import Table
from django.contrib.auth.decorators import login_required

#-------------------------------------------------------

# Create your views here.
def about_turno(request,id):
    try:
       turno = Turno.objects.get(id=id)       
    except Turno.DoesNotExist:
       turno = None
    turno = Turno.objects.all().exclude(habilitada=True).order_by("fecha").reverse()
