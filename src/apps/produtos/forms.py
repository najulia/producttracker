from django import forms
from apps.produtos.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["titulo", "slug", "preco","descricao", "foto", "quantidade", "em_estoque"]
