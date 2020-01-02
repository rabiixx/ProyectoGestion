from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tabla/$', views.TablaListView.as_view(), name='tabla'),
	url(r'^tabla/(?P<pk>\d+)$', views.TablaDetailView.as_view(), name='tabla-detail'), 
    url(r'^tabla/(?P<pk>[-\w]+)/renew/$', views.renew_tabla, name='renew-tabla'),
    url(r'^prueba/$', views.prueba, name='prueba'),
    path('radio', views.radio_buttons, name='radio_buttons'),

]