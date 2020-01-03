from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tabla/$', views.TablaListView.as_view(), name='tabla'),
	url(r'^tabla/(?P<pk>\d+)$', views.TablaDetailView.as_view(), name='tabla-detail'), 
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^calculator/$', views.calculator, name='calculator'),
    url(r'^agua/$', views.agua, name='agua'),
    url(r'^vehiculos/$', views.vehiculos, name='vehiculos'),
    url(r'^edificios/$', views.edificios, name='edificios'),
    url(r'^consumoElectricidad/$', views.consumoElectricidad, name='consumoElectricidad'),
    url(r'^calefaccion/$', views.calefaccion, name='calefaccion'),
    url(r'^personal/$', views.personal, name='personal'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]