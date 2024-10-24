from django.forms import *
from .models import Produto
from django.core.exceptions import ValidationError
class ProdutoForm(ModelForm):
    class Meta:
       model = Produto
       fields = ['nome','marca','preco','estoque']
    
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        
        if len(nome) < 3 or nome == '' or nome == ' ':
            raise ValidationError('Nome do produto possui menos que 3 caracteres ou esta em branco! Corrija tal erro')
        
        return nome 