from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tabla/$', views.TablaListView.as_view(), name='tabla'),
	url(r'^tabla/(?P<pk>\d+)$', views.TablaDetailView.as_view(), name='tabla-detail'), 
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^accederCuenta/$', views.accederCuenta, name='accederCuenta'),
    url(r'^cuenta/(?P<nombre>\w*)/$', views.TestUsuarioListView.as_view(), name='cuenta'),
    url(r'^calculator/$', views.calculator, name='calculator'),
    url(r'^test/$', views.test, name='test'),
    url(r'^agua/(?P<nombreTest_id>\w*)/$', views.agua, name='agua'),
    url(r'^vehiculos/(?P<nombreTest_id>\w*)/$', views.vehiculos, name='vehiculos'),
    url(r'^vehiculospregunta/(?P<nombreTest_id>\w*)/$', views.vehiculospregunta, name='vehiculospregunta'),
    url(r'^edificios/(?P<nombreTest_id>\w*)/$', views.edificios, name='edificios'),
    url(r'^consumoElectricidad/(?P<nombreTest_id>\w*)/$', views.consumoElectricidad, name='consumoElectricidad'),
    url(r'^calefaccion/(?P<nombreTest_id>\w*)/$', views.calefaccion, name='calefaccion'),
    url(r'^personal/(?P<nombreTest_id>\w*)/$', views.personal, name='personal'),
    url(r'^viajes/(?P<nombreTest_id>\w*)/$', views.viajes, name='viajes'),
    url(r'^generacionElectricidad/(?P<nombreTest_id>\w*)/$', views.generacionElectricidad, name='generacionElectricidad'),
    url(r'^resultado/(?P<nombreTest_id>\w*)/$', views.resultado, name='resultado'),
    url(r'^ConsumoAguaDetail/(?P<pk>\d+)$', views.ConsumoAguaDetailView.as_view(), name='ConsumoAguaDetail'),
    url(r'^ConsumoAguaModify/(?P<pk>\d+)$', views.ConsumoAguaModify, name='ConsumoAguaModify'),
    url(r'^testDetallado/(?P<nomtest>\w*)/$', views.TestDetallado, name='TestDetallado'),
]