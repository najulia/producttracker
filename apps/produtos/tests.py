from django.test import TestCase
from apps.produtos.models import Produto

class TestProdutoModel(TestCase):

    def test_testando_a_criacao_de_produto(self):
        p = Produto.objects.create()
        p.save()
        assert p is not None




