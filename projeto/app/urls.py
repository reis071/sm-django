from django.urls import path
from . import views

urlpatterns = [
    path('listar_produtos',views.buscar_todos_os_produtos),
    path('cadastrar_produto',views.cadastrar_produto),
]
