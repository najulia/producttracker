from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages


class UserLoginView(LoginView):
    template_name = "users/login.html"
    next_page = "produto-list"

class UserCadastroView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'users/cadastro.html'
    success_url = reverse_lazy('login')

class UserLogoutView(LogoutView):
    next_page = 'logout'
    template_name = 'users/logout.html'
    def get(self, request, *args, **kwargs):
        # Adiciona a mensagem antes de chamar o método pai
        messages.success(request, "Logout realizado com sucesso")
        return super().get(request, *args, **kwargs)

class UserPasswordReset(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'users/password_reset.html'

class UserPasswordResetDone(PasswordResetDoneView):
    template_name = 'reset_done.html'

class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'users/painel_usuarios.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class UserDetailView(LoginRequiredMixin, generic.DetailView):
    """Retorna o perfil de um usuário conforme ID passado na URL"""
    model = User
    template_name = 'users/user_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = User
    permission_required = ["produtos.change.user"]
    fields = ['username', 'is_staff','is_active', 'is_superuser', 'first_name', 'email']
    template_name = "users/user_update_form.html"
    success_url = reverse_lazy('usuarios-lista')
