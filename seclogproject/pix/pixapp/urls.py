# pixapp/urls.py
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from pixapp import views

urlpatterns = [
	url(r'^$', auth_views.login),
	url(r'^index.html', auth_views.login),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^logout.html', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^home.html',views.pixpage1.as_view()),
    url(r'^ip.html',views.ip.as_view()),
	url(r'^submitIP$',views.submitIP.as_view()),
	url(r'^nova1.html',views.pixpage2.as_view()),
	url(r'^cinder1.html',views.pixpage3.as_view()),
	url(r'^neutron1.html',views.pixpage4.as_view()),
	url(r'^glance1.html',views.pixpage5.as_view()),
	url(r'^keystone1.html',views.pixpage6.as_view()),
	url(r'^logs.html',views.pixpage7.as_view()),
]