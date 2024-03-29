from django.urls import path
from . import views
urlpatterns = [

    path('', views.authlogin, name="login"),
    path('forgetpassword/', views.authforgetpassword, name="Forget password"),
    path('registration/', views.authregistration, name="registration"),
    path('logout/', views.authlogout, name="Logout"),

    

    

]