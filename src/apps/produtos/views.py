from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from apps.produtos.models import Produto
from apps.produtos.forms import ProdutoForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from uuid import uuid4
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect


def index(request):
    return redirect('login')

class ProdutoFormView(FormView):
    form = ProdutoForm()
    template_name = "produto_form.html"

class ProdutoDetailView(LoginRequiredMixin, DetailView):
    """Retorna as especificações de um produto conforme o slug passado na URL"""
    model = Produto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProdutoListView(LoginRequiredMixin, ListView):
    """Retorna uma lista de todos os produtos"""
    model = Produto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProdutoCreateView(PermissionRequiredMixin, CreateView):
    model = Produto
    fields = ["titulo", "preco","descricao", "foto", "quantidade"]
    success_url = reverse_lazy('produto-list')

    permission_required = ["produtos.add.produto", "produtos.view.produto"]

    def form_valid(self, form):
        instance = form.instance
        instance.slug = gerar_slug(instance.titulo)
        return super().form_valid(form)
    
class ProdutoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Produto
    fields = ["titulo", "preco","descricao", "foto", "quantidade"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('produto-list')
    permission_required = ["produtos.change.produto"]

    def form_valid(self, form):
        instance = form.instance
        instance.slug = gerar_slug(instance.titulo)
        return super().form_valid(form)

class ProdutoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Produto
    success_url = reverse_lazy('produto-list')
    permission_required = ["produtos.delete.produto"]


def gerar_slug(titulo):
    """Função para gerar o slug automaticamente antes de enviar/atualizar o produto"""
    slug = slugify(titulo)
    # Verifica se o slug já existe
    if Produto.objects.filter(slug=slug).exists():
        # Gera um novo slug
        slug = slugify(titulo) + "-" + str(uuid4())

    return slug

def verifica_tamanho_foto(foto):
    """Função para verificar o tamanho da foto antes de enviar/atualizar produto"""
    if foto.size > 1024 * 1024 * 1:
        return False
    return True
