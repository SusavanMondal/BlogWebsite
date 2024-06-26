from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls'), name="home"),
    # path('login/', views.login),
    # path('logout/', views.logout),
    path('employee/', include('employee.urls')),
    path('contactus/', include('contact.urls')),
    path('authentication/', include('authentication.urls')),
    
    
     
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

