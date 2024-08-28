from django.contrib import admin
from apps.produtos.models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Produto, ProdutoAdmin)
