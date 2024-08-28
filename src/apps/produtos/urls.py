from django.urls import path
from apps.produtos.views import ProdutoDetailView, ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path("", ProdutoListView.as_view(), name="produto-list"),
    path("criar/", ProdutoCreateView.as_view(), name='produtos-create'), 
    path("editar/<slug:slug>/", ProdutoUpdateView.as_view(), name='produtos-update'), 
    path("excluir/<slug:slug>/", ProdutoDeleteView.as_view(), name='produtos-delete'), 
    path("<slug:slug>/", ProdutoDetailView.as_view(), name="produto-detail"),
]