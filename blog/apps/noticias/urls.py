from django.urls import path, include
from . import views

app_name = 'noticias'

urlpatterns = [
    
    path('', views.Noticias, name='noticias'),
    path('Detalle/<int:pk>', views.Detalle_Noticias, name='detalle'),    
]