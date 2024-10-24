from django.urls import path
from . import views

urlpatterns = [
    path('listar_produtos',views.buscar_todos_os_produtos, name= 'rota_lista_de_produtos'),
    path('cadastrar_produto',views.cadastrar_produto,name='rota_de_cadastrar_produto'),
    path('cadastar_usuario',views.cadastrar_usuario),
    path('logar_usuario',views.login_usuario, name='rota_login'),
]
