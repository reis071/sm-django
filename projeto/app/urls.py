from django.urls import path
from . import views

urlpatterns = [
    path('listar_produtos',views.buscar_todos_os_produtos),
    path('cadastrar_produto',views.cadastrar_produto),
    path('atualizar/<int:produto_id>',views.atualizar_produto),
    # path('produto_estatico',views.produtos_estaticos),
    # path('lista_de_roupa_rota',views.listar_roupas),
]
