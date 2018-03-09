from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^subscribe$', views.subscribe, name='subscribe'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^product/(?P<id>\d+)/$', views.product_card, name='product_card'),
    url(r'^add_to_cart/(?P<id>\d+)/$', views.add_to_cart, name='add_to_cart'),
    url(r'^checkout$', views.checkout, name='checkout'),
    url(r'^remove_from_cart/(?P<id>\d+)/$', views.remove_from_cart, name='remove_from_cart'),
    url(r'^remove_cart/$', views.remove_cart, name='remove_cart'),
    url(r'^order_detail/$', views.order_detail, name='order_detail'),
    url(r'^watches/(?P<id>\d+)/$', views.watches, name='watches'),

]
