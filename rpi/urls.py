from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$',views.addrpi,name="addrpi"),
    url(r'^lifesign',views.lifesign,name='lifesign')
]
