from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth


urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', views.Home, name='home'),
    path('Nosotros/', views.Nosotros, name='nosotros'),
    
    #URL LOGIN/LOGOUT
    path('login/', auth.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),

    #URL DE APLICACIONES
    path('Noticias/', include('apps.noticias.urls')),
    path('Usuario/', include('apps.usuarios.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)