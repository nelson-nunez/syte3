
#url campaing
from django.conf.urls import url
from . import views

app_name = 'app_turnos'

urlpatterns = [

    #home publica##################
    
	url(r'^about_turno/(?P<id>\d+)/$', views.about_turno, name="about_turno"),	


	
			
]
