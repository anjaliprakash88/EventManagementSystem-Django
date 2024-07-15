from django.urls import path
from . import views

urlpatterns = [
    path('user', views.reg_user, name ='user'),
    path('user_login', views.user_login, name ='user_login'),
    path('user_logout', views.user_logout, name ='user_logout'),
    path('', views.home, name='home'),
    path('about', views.about, name ='about'),
    path('booking', views.booking, name ='booking'),
    path('events', views.events, name ='events'),
    path('contact', views.contact, name ='contact'),
]