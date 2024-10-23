from django.forms import *
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
       model = Produto
       fields = ['nome','marca','preco','estoque']
    
    
    