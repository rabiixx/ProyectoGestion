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
    path('radio', views.radio_buttons, name='radio_buttons'),
]