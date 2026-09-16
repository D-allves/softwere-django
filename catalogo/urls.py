from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_jogos, name='lista_jogos'),
    path('adicionar/', views.adicionar_jogo, name='adicionar_jogo'),
    path('excluir/<int:id>/', views.excluir_jogo, name='excluir_jogo'),
]