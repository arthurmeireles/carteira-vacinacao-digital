from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from django.shortcuts import render


urlpatterns = [
    # ESSA ROTA CRIA TODOS OS TIPOS DE USUARIOS E LISTA TODOS ELES
    path('registro', Registro.as_view()),
    #retorna todos os usuarios
    path('usuario', UsuarioList.as_view()),
    #Edita um usuario
    # path('usuario/<int:pk>', UsuarioDetail.as_view()),
    # Cria Associação e Remove Associação entre profissional e um estabelecimento
    path('associar-profissional/<int:pk_profissional>/<int:pk_estabelecimento>', AssociarProfissionalEstabelecimento.as_view()),

    # ESSA ROTA CRIA AS VACINAS E LISTA TODAS ELAS
    path('vacina', VacinaList.as_view()),

    path('municipio', MunicipioList.as_view()),
    
    path('estabelecimento', EstabelecimentoList.as_view())


]
