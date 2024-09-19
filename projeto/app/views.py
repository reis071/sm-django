from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

lista_de_produtos = ['salame', 'pao', 'guarana antartica']


def buscar_todos_os_produtos(request):
    if request.method == 'GET':
        return JsonResponse( {'produtos':lista_de_produtos} )
    else:
        return JsonResponse({'erro':'requisicao Invalida'}, status = 405)

@csrf_exempt
def cadastrar_produto(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)  # Lê o corpo da requisição JSON
            novo_produto = body.get('nome')
            if novo_produto:
                lista_de_produtos.append(novo_produto)
                return JsonResponse({'mensagem': 'Produto adicionado', 'produtos': lista_de_produtos})
            else:
                return JsonResponse({'erro': 'Nome do produto não informado'}, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'JSON inválido'}, status=400)
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)