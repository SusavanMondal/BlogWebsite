
from django.urls import path
from . import views
urlpatterns = [

    # path('contactus', views.contactus, name="contact"),
    path('aboutus', views.aboutus, name="about"),
    path('', views.home, name="home"),
    

]