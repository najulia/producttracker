from django.db import models
from django.utils.text import slugify

class Produto(models.Model):
    """Classe para representar um produto"""
    titulo = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200)
    preco = models.FloatField()
    descricao = models.TextField()
    foto = models.FileField(upload_to="produtos")
    quantidade = models.IntegerField(default=0)
    em_estoque = models.BooleanField(blank=True, default=False)

    def produto_em_estoque(self):
        """Função para verificar se o produto está em estoque ou não"""
        if int(self.quantidade) > 0:
            self.em_estoque = True
            return f"Temos {self.quantidade} unidades desse produto"
        else:
            self.em_estoque = False
            return "Produto não está disponível"


    def __str__(self) -> str:
        return f"{self.titulo} - R$ {self.preco} - Estoque: {self.quantidade} unidades"
