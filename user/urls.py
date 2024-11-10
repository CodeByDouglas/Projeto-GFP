from django.urls import path
from .views import CustomLoginView, dashboard, cadastrar_usuario
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('cadastro/', cadastrar_usuario, name='cadastrar'),
    path('despesa-fixa/', views.lancar_despesa_fixa, name='despesa_fixa'),
    path('despesa-parcelada/', views.lancar_despesa_parcelada, name='despesa_parcelada'),
    path('despesa-comum/', views.lancar_despesa_comum, name='despesa_comum'),
    path('perfil/', views.perfil, name='perfil'),
    path('alterar-senha/', auth_views.PasswordChangeView.as_view(
        template_name='alterar_senha.html',
        success_url='/perfil/'
    ), name='alterar_senha'),
    path('alterar-nome/', views.alterar_nome, name='alterar_nome'),
    path('alterar-renda/<int:renda_id>/', views.alterar_renda, name='alterar_renda'),
    path('trilha/', views.trilha_view, name='trilha'),
    path('extrato/', views.extrato_view, name='extrato'),
    path('delete_despesas/', views.delete_despesas, name='delete_despesas'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Adicione esta linha
]