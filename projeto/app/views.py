from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Produto

#Serve como um protetor no qual nao vai permitir interceptacoes no meio da requisicao do
#usuario
@csrf_exempt
@require_http_methods(["GET"])
def buscar_todos_os_produtos(request):
    produtos = Produto.objects.all().values() #pegando todos os objetos Produto
    return JsonResponse( list(produtos), safe=False ) #retornar uma lista de Produtos
    
@csrf_exempt
@require_http_methods(["POST"])
def cadastrar_produto(request):
   dados = json.loads(request.body)
   produto = Produto.objects.create( 
                                    nome=dados.get('nome'),
                                    marca = dados.get('marca'),
                                    preco = dados.get('preco'),
                                    estoque = dados.get('estoque')
                                    )
   return JsonResponse({"id":produto.id, 
                        "mensagem":"Produto criado com sucesso!!!"}
                       )
   
# Exclui a verificação de token CSRF para esta view (cuidado ao usar em produção)
@csrf_exempt
# Restringe a função para aceitar apenas requisições do tipo PUT
@require_http_methods(["PUT"])
def atualizar_produto(request, produto_id):
    try:
        # Tenta obter o produto com o ID fornecido; lança uma exceção se o produto não existir
        produto = Produto.objects.get(id=produto_id)
        
        # Carrega os dados JSON recebidos no corpo da requisição
        dados = json.loads(request.body)
        
        # Atualiza os campos do produto com os valores recebidos, mantendo os antigos se os novos não forem fornecidos
        produto.nome = dados.get('nome', produto.nome)           # Atualiza o nome, se fornecido
        produto.marca = dados.get('marca', produto.marca) # Atualiza a descrição, se fornecida
        produto.preco = dados.get('preco', produto.preco)         # Atualiza o preço, se fornecido
        produto.estoque = dados.get('estoque', produto.estoque)   # Atualiza o estoque, se fornecido
        
        # Salva as mudanças no banco de dados
        produto.save()
        
        # Retorna uma resposta JSON indicando que o produto foi atualizado com sucesso
        return JsonResponse({"message": "Produto atualizado com sucesso!"})
    
    # Caso o produto com o ID fornecido não exista, retorna uma resposta de erro 404
    except Produto.DoesNotExist:
        return JsonResponse({"error": "Produto não encontrado"}, status=404)
