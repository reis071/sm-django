from django.urls import path
from . import views

urlpatterns = [
    path('listar_produtos',views.buscar_todos_os_produtos),
    path('cadastrar_produto',views.cadastrar_produto),
    path('atualizar/<int:produto_id>',views.atualizar_produto),
    path('tupla_de_produtos_estaticos',views.produtos_estaticos)
]
