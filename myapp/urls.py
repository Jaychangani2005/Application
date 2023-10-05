from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('home/', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('services/', views.Services, name='services'),
    path('video-record/', views.VideoRecord, name='video_record'),
    path('audio-record/', views.AudioRecord, name='audio_record'),
    path('click-photos/', views.ClickPhotos, name='click_photos'),
    path('contact/', views.Contact, name='contact'),
]
