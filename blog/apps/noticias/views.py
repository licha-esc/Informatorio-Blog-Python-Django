from django.shortcuts import render
from .models import Noticia
# from django.contrib.auth.decorators import login_required


# @login_required #sirve para que no se pueda acceder a una página sin loguearse
def Noticias(request):
    contexto = {}
    n = Noticia.objects.all() # Retorna una lista de objetos
    contexto['noticias'] = n
    
    return render(request, 'noticias/noticias.html', contexto)

def Detalle_Noticias(request, pk):
    contexto = {}
    n = Noticia.objects.get(pk=pk) # Retorna un solo objeto
    contexto['noticia'] = n
    
    return render(request, 'noticias/detalle.html', contexto)