from django.urls import path
from apps.users.views import UserLoginView, UserCadastroView, UserLogoutView, UserPasswordReset, UserPasswordResetDone, PasswordResetConfirmView, UserListView, UserUpdateView, UserDetailView


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("cadastro/", UserCadastroView.as_view(), name="cadastro"),
    path("logout/", UserLogoutView.as_view(), name='logout'),
    path("reset/", UserPasswordReset.as_view(), name='reset'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', UserPasswordResetDone.as_view(), name='reset_done'),
    path('painel/', UserListView.as_view(), name='usuarios-lista'),
    path('painel/<int:pk>', UserDetailView.as_view(), name='usuarios-detail'),
    path('editar/<int:pk>', UserUpdateView.as_view(), name='usuarios-update'),
]