
from django.urls import path
from . import views

urlpatterns = [
    
    
    path('', views.login),
    path('profile/', views.profile, name="profile"),
    
     
]