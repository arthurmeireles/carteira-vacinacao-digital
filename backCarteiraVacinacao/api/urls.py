from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from django.shortcuts import render


urlpatterns = [

    # Login - Logout
    path('login', CustomAuthToken.as_view()),
    # path('logout', Logout.as_view()),

    # ESSA ROTA CRIA TODOS OS TIPOS DE USUARIOS E LISTA TODOS ELES
    path('registro', Registro.as_view()),
    #retorna todos os USUARIOS
    path('usuario', UsuarioList.as_view()),
    # Cria Associação e Remove Associação entre profissional e um estabelecimento
    path('associar-profissional/<int:pk_profissional>/<int:pk_estabelecimento>', AssociarProfissionalEstabelecimento.as_view()),

    # ESSA ROTA CRIA AS VACINAS E LISTA TODAS ELAS
    path('vacina', VacinaList.as_view()),
    path('vacina/<int:pk>', EditDeleteVacina.as_view()),
    path('vacinaBusca', BuscaVacina.as_view()),
    path('municipio', MunicipioList.as_view()),
    
    path('estabelecimento', EstabelecimentoList.as_view()),

    path('vacinaestabelecimento', VacinaEstabelecimento.as_view()),
    path('vacinaestabelecimento/<int:pk>', getVacinaEstabelecimento.as_view()),

    #Lista todos os PROFISSIONAIS
    path('profissional', ProfissionalList.as_view()),
    
    #Lista todos os PACIENTES
    path('paciente', PacienteList.as_view()),
    path('carteira-vacinacao', CarteiraVacinacaoList.as_view()),

    # Criar AGENDAMENTO e lista todos os AGENDAMENTOS
    path('agendamento', AgendamentoList.as_view()),
    path('agendamentoDisponivel', AgendamentosDisponivel.as_view()),
    path('agendamentoMarcados', AgendamentosMarcado.as_view()),
    path('agendamentoPaciente/<int:pk>', AgendamentosPaciente.as_view()),
    path('agendamento/<int:pk>', EditDeleteAgendamento.as_view()),

    # path('buscarProfissional', buscarProfissional.as_view()),
    path('buscarProfissionalPorCPF/<str:cpf>', buscarProfissionalPorCPF.as_view()),
    # path('buscarEstabelecimento', buscarEstabelecimento.as_view()),
    path('buscarEstabelecimentoPorCNES/<str:cnes>', buscarEstabelecimentoPorCNES.as_view()),


    # Associa um PACIENTE a um AGENDAMENTO - Função de Agendar
    path('associar-paciente/<int:pk_usuario>/<int:pk_agendamento>', AssociarPacienteAgendamento.as_view()),

    # Cria uma APLICACAO     
    path('aplicacao', AplicacaoCriacao.as_view()),
    # Retorna APLICACOES do PACIENTE
    path('aplicacao/<int:pk>', AplicacoesPaciente.as_view()),


    path('query/<str:nome>', pegaQuery.as_view()),


]
