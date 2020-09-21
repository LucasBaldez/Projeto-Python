from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Fornecedores/', views.List_Fornecedores, name='List_Fornecedores'),
    path('Criar_Fornecedor/', views.Criar_fornecedor, name='Criar_fornecedor')
    
]