
from django.urls import path
from local_connect import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('community-hub', views.community_hub, name='community_hub'),
    path('business-profile', views.business_profile, name='business_profile'),
    path('profile', views.profile, name='profile'),
    path('events', views.events, name='events'),


]