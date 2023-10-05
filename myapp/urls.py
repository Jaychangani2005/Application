from django.contrib import admin
from django.urls import path
from myapp import views
 
urlpatterns =[
    path('',views.index, name='index'),

    path('about',views.about, name='about'),
    # path('home',views.home, name='home'),

    
    path('services',views.services, name='services'),
    path('VideoRecord',views.VideoRecord, name='VideoRecord'),
    path('VoiceRecord',views.VoiceRecord, name='VoiceRecord'),
    path('ClickPhotos',views.ClickPhotos, name='ClickPhotos'),


    path('contact',views.contact, name='contact '),

]