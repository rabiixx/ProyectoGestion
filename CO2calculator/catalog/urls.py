from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^constantesRedirect/$', views.constantesRedirect, name='constantesRedirect'),
    url(r'^tablaconstantesDetail/(?P<pk>\d+)/$', views.constantesDetailView.as_view(), name='constantesDetail'),
    url(r'^constantesModify/(?P<pk>\d+)/$', views.constantesModify, name='constantesModify'),
    url(r'^accederCuenta/$', views.accederCuenta, name='accederCuenta'),
    url(r'^cuenta/(?P<nombre>\w*)/$', views.TestUsuarioListView.as_view(), name='cuenta'),
    url(r'^calculator/$', views.calculator, name='calculator'),

    url(r'^test/$', views.test, name='test'),
    url(r'^agua/(?P<nombreTest_id>\w*)/$', views.agua, name='agua'),
    url(r'^vehiculos/(?P<nombreTest_id>\w*)/$', views.vehiculos, name='vehiculos'),
    url(r'^vehiculospregunta/(?P<nombreTest_id>\w*)/$', views.vehiculospregunta, name='vehiculospregunta'),
    url(r'^viajespregunta/(?P<nombreTest_id>\w*)/$', views.viajespregunta, name='viajespregunta'),
    url(r'^edificios/(?P<nombreTest_id>\w*)/$', views.edificios, name='edificios'),
    url(r'^consumoElectricidad/(?P<nombreTest_id>\w*)/$', views.consumoElectricidad, name='consumoElectricidad'),
    url(r'^calefaccion/(?P<nombreTest_id>\w*)/$', views.calefaccion, name='calefaccion'),
    url(r'^personal/(?P<nombreTest_id>\w*)/$', views.personal, name='personal'),
    url(r'^viajes/(?P<nombreTest_id>\w*)/$', views.viajes, name='viajes'),
    url(r'^generacionElectricidad/(?P<nombreTest_id>\w*)/$', views.generacionElectricidad, name='generacionElectricidad'),
    url(r'^resultado/(?P<nombreTest_id>\w*)/$', views.resultado, name='resultado'),
    url(r'^compensacion/(?P<nombreTest_id>\w*)/$', views.compensacion, name='compensacion'),

    url(r'^testDetallado/(?P<nomtest>\w*)/$', views.TestDetallado, name='TestDetallado'),
    url(r'^ConsumoAguaDetail/(?P<pk>\d+)$', views.ConsumoAguaDetailView.as_view(), name='ConsumoAguaDetail'),
    url(r'^ConsumoAguaModify/(?P<pk>\d+)$', views.ConsumoAguaModify, name='ConsumoAguaModify'),
    url(r'^ConsumoVehiculoList/(?P<nomtest>\w*)$', views.ConsumoVehiculoListView.as_view(), name='ConsumoVehiculoList'),
    url(r'^ConsumoVehiculoDetail/(?P<pk>\d+)$', views.ConsumoVehiculoDetailView.as_view(), name='ConsumoVehiculoDetail'),
    url(r'^ConsumoVehiculoModify/(?P<pk>\d+)$', views.ConsumoVehiculoModify, name='ConsumoVehiculoModify'),
    url(r'^ConsumoElectricidadDetail/(?P<pk>\d+)$', views.ConsumoElectricidadDetailView.as_view(), name='ConsumoElectricidadDetail'),
    url(r'^ConsumoElectricidadModify/(?P<pk>\d+)$', views.ConsumoElectricidadModify, name='ConsumoElectricidadModify'),
    url(r'^ConsumoCalefaccionDetail/(?P<pk>\d+)$', views.ConsumoCalefaccionDetailView.as_view(), name='ConsumoCalefaccionDetail'),
    url(r'^ConsumoCalefaccionModify/(?P<pk>\d+)$', views.ConsumoCalefaccionModify, name='ConsumoCalefaccionModify'),
    url(r'^PersonalEmpresaDetail/(?P<pk>\d+)$', views.PersonalEmpresaDetailView.as_view(), name='PersonalEmpresaDetail'),
    url(r'^PersonalEmpresaModify/(?P<pk>\d+)$', views.PersonalEmpresaModify, name='PersonalEmpresaModify'),
    url(r'^ViajesEmpresaList/(?P<nomtest>\w*)$', views.ViajesEmpresaListView.as_view(), name='ViajesEmpresaList'),
    url(r'^ViajesEmpresaDetail/(?P<pk>\d+)$', views.ViajesEmpresaDetailView.as_view(), name='ViajesEmpresaDetail'),
    url(r'^ViajesEmpresaModify/(?P<pk>\d+)$', views.ViajesEmpresaModify, name='ViajesEmpresaModify'),
    url(r'^ConsumoEdificiosDetail/(?P<pk>\d+)$', views.ConsumoEdificiosDetailView.as_view(), name='ConsumoEdificiosDetail'),
    url(r'^ConsumoEdificiosModify/(?P<pk>\d+)$', views.ConsumoEdificiosModify, name='ConsumoEdificiosModify'),
    url(r'^GeneracionElectricidadDetail/(?P<pk>\d+)$', views.GeneracionElectricidadDetailView.as_view(), name='GeneracionElectricidadDetail'),
    url(r'^GeneracionElectricidadModify/(?P<pk>\d+)$', views.GeneracionElectricidadModify, name='GeneracionElectricidadModify'),
]