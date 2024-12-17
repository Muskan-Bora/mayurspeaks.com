from django.urls import path, include
from mayurweb import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('about_me/', views.about_me, name='about_me'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('services/<int:servicepage_id>/', views.services, name='service_detail'),
    path('coaching_service/', views.coaching_service, name='coaching_service'),
    path('keynotespeak_service/', views.keynotespeak_service, name='keynotespeak_service'),
    path('motivate_service/', views.motivate_service, name='motivate_service'),
]