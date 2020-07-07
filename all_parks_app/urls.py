from django.urls import path
from . import views

urlpatterns= [
    path('', views.index),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about'),
    path('disney', views.disney, name='disney'),
    path('universal', views.universal, name='universal'),
    path('contact', views.contact, name='contact'),
    path('main', views.main, name='main')
]