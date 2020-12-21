from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView



from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ViewSet

import django_filters.rest_framework

from .models import *
from .pagination import *
from .serializers import *
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


# Create your views here.

class Registro(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroSerializer
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        if instance.tipo_usuario == 1:
            Coordenador.objects.create(usuario=instance)
        elif instance.tipo_usuario == 2:
            Profissional.objects.create(usuario=instance)
        elif instance.tipo_usuario == 3:
            Paciente.objects.create(usuario=instance)
        instance.save()

# ----------------- COORDENADOR ------------------------

class CoordenadorList(ListCreateAPIView):
    serializer_class = CoordenadorSerializer
    pagination_class = PaginationDefault
    queryset = Coordenador.objects.all().reverse().order_by('id')

# ---------------------------

class ProfissionalList(ListCreateAPIView):
    estabelecimento = EstabelecimentoSerializer()
    def post(self, request, format=None):
        serializer = ProfissionalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    



    
class AssociarProfissionalEstabelecimento(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        try:
            profissional = Profissional.objects.get(usuario_id = kwargs.get('pk_profissional'))
            estabelecimento =  Estabelecimento.objects.get(pk = kwargs.get('pk_estabelecimento'))
            if profissional.estabelecimento:
                return Response('Não foi possível associar o profissional. Já há uma associacao com um estabelecimento',
                                status=status.HTTP_401_UNAUTHORIZED)
            elif estabelecimento:
                profissional.estabelecimento = estabelecimento
                profissional.save()
                return Response({"sucesso": ("O estabelecimento foi associado.")}, status=status.HTTP_200_OK)
            else:
                return Response('Estabelecimento não existe', status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    @staticmethod
    def delete(request, *args, **kwargs):
        try:
            estabelecimento =  Estabelecimento.objects.get(pk=kwargs.get('pk_estabelecimento'))
            profissional = Profissional.objects.get(usuario_id=kwargs.get('pk_profissional'))
            if profissional.estabelecimento:
                profissional.estabelecimento = None
                profissional.save()
                return Response('Removida associacao entre Profissional e Estabelecimento', status=status.HTTP_200_OK)
            else:
                return Response('O profissional não possui associação com um estabelecimento', status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ---------------------------

class PacienteList(ListCreateAPIView):
    serializer_class = PacienteSerializer
    pagination_class = PaginationDefault
    queryset = Paciente.objects.all().reverse().order_by('id')

class CarteiraVacinacaoList(ListCreateAPIView):
    serializer_class = CarteiraVacinacaoSerializer
    pagination_class = PaginationDefault
    queryset = CarteiraVacinacao.objects.all().reverse().order_by('id')

class AssociarPacienteAgendamento(APIView): # Vincula um paciente a um Agendamento
    @staticmethod
    def post(request, *args, **kwargs):
        try:
            paciente = Paciente.objects.get(usuario_id = kwargs.get('pk_usuario'))
            agendamento =  Agendamento.objects.get(pk = kwargs.get('pk_agendamento'))
            if agendamento.paciente:
                return Response('Não foi possível agendar o horário para o Paciente. O Paciente já agendou o horario',
                                status=status.HTTP_401_UNAUTHORIZED)
            elif agendamento:
                agendamento.paciente = paciente
                agendamento.save()
                return Response({"sucesso": ("O agendamento foi realizado.")}, status=status.HTTP_200_OK)
            else:
                return Response('Agendamento não existe', status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    @staticmethod
    def delete(request, *args, **kwargs):
        try:
            paciente = Paciente.objects.get(usuario_id = kwargs.get('pk_usuario'))
            agendamento =  Agendamento.objects.get(pk = kwargs.get('pk_agendamento'))

            if agendamento.paciente:
                agendamento.paciente = None
                agendamento.save()
                return Response('Agendamento Removido', status=status.HTTP_200_OK)
            else:
                return Response('O paciente não possui agendamento', status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ---------------- AGENDAMENTOS ----------------------

class AgendamentoList(APIView):
    def get(self, request, format=None):
        agendamentos = Agendamento.objects.all()
        serializer = AgendamentoListagem(agendamentos, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AgendamentoCriacao(data = request.data)
        if serializer.is_valid():
            serializer.save(paciente_id = request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AgendamentosDisponivel(APIView):
    def get(self, request, format=None):
        agendamentos = Agendamento.objects.filter(aberto = True)
        serializer = AgendamentoListagem(agendamentos, many=True)
        return Response(serializer.data)

class AgendamentosMarcado(APIView):
    def get(self, request, format=None):
        agendamentos = Agendamento.objects.filter(aberto = False)
        serializer = AgendamentoListagem(agendamentos, many=True)
        return Response(serializer.data)

class EditDeleteAgendamento(APIView):
    def get_object(self,pk):
        try:
            return Agendamento.objects.get(pk=pk)
        except Agendamento.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        agendamento = self.get_object(pk)
        serializer = AgendamentoSerializer(agendamento)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        agendamento = self.get_object(pk)
        serializer = EditarAgendamentoSerializer(agendamento, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, **kwargs):
        agendamento = Agendamento.objects.get(pk = kwargs.get('pk'))
        agendamento.delete()
        return Response('Agendamento Deletado', status=status.HTTP_200_OK)

class AgendamentosPaciente(APIView):
    def get(self, request, **kwargs):
        paciente = Paciente.objects.get(usuario_id = kwargs.get('pk'))
        agendamentos = Agendamento.objects.filter(paciente = paciente)
        serializer = AgendamentoListagem(agendamentos, many=True)
        return Response(serializer.data)






# ---------------- APLICAÇÕES ----------------------

class AplicacaoCriacao(APIView):
    def decrementarQuantidade(self, pk_vacina):
        vacina_estabelecimento = Vacina_Estabelecimento.objects.get(pk = pk_vacina)
        vacina_estabelecimento.quantidade = vacina_estabelecimento.quantidade - 1 
        vacina_estabelecimento.save()

    def post(self, request, *args, **kwargs):
        serializer = AplicacaoCriacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            self.decrementarQuantidade(request.data.get('vacina'))
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, *args, **kwargs):
        queryset = Aplicacao.objects.all().reverse()
        serializer = AplicacaoSerializer(queryset, many=True)
        return Response(serializer.data)


class AplicacoesPaciente(APIView):
    def get(self,request, **kwargs):
        paciente = Paciente.objects.get(usuario_id = kwargs.get('pk'))
        carteiraVacinacao = CarteiraVacinacao.objects.get(paciente= paciente)
        aplicacoesPaciente = Aplicacao.objects.filter(carteiraVacinacao = carteiraVacinacao)
        serializer = AplicacaoSerializer(aplicacoesPaciente, many=True)
        return Response(serializer.data)

# ---------------------------

class UsuarioList(ListCreateAPIView):
    serializer_class = UsuarioSerializer
    pagination_class = PaginationDefault
    queryset = Usuario.objects.all().reverse().order_by('id')

class VacinaList(ListCreateAPIView):
    def post(self, request):
        serializer = VacinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def get(self, *args, **kwargs):
        queryset = Vacina.objects.all().reverse()
        serializer = VacinaSerializer(queryset, many=True)
        return Response(serializer.data)

class BuscaVacina(ListAPIView):
    queryset = Vacina.objects.all().reverse().order_by('id')
    serializer_class = BuscaVacinaSerializer
    pagination_class = PaginationDefault
    filter_backends = (SearchFilter,)
    search_fields = ['nome']


class VacinaEstabelecimento(APIView):
    serializer_class = VacinaEstabelecimentoSerializer
    pagination_class = PaginationDefault
    queryset = Vacina_Estabelecimento.objects.all().reverse().order_by('id')

class getVacinaEstabelecimento(APIView):
    def get(self, *args, **kwargs):
        estoque_estabelecimento = Vacina_Estabelecimento.objects.filter(vacina_id = kwargs.get('pk'))
        serializer = ListaVacinaEstabelecimentoSerializer(estoque_estabelecimento, many=True)
        return Response(serializer.data)



class EditDeleteVacina(APIView):
    def put(self, request, **kwargs):
        vacina = Vacina.objects.get(pk = kwargs.get('pk'))
        serializer = EditarVacinaSerializer(vacina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, **kwargs):
        vacina = Vacina.objects.get(pk = kwargs.get('pk'))
        vacina.delete()
        return Response('Vacina Deletada', status=status.HTTP_200_OK)
# ---------------------------

class MunicipioList(ListCreateAPIView):
    serializer_class = MunicipioSerializer
    pagination_class = PaginationDefault
    queryset = Municipio.objects.all().reverse().order_by('id')

class EstabelecimentoList(ListCreateAPIView):
    serializer_class = EstabelecimentoSerializer
    pagination_class = PaginationDefault
    queryset = Estabelecimento.objects.all().reverse().order_by('id')

# ---------------------------


class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        usuario = UsuarioSerializer(user)
        return Response({
            'token': token.key,
            'usuario': usuario.data
        })

class pegaQuery(APIView):
    def get(self,request,*args, **kwargs):
        estoque_estabelecimento = Vacina_Estabelecimento.objects.filter(estabelecimento_id = kwargs.get('pk')).query
        print(estoque_estabelecimento)

        serializer = ListaVacinaEstabelecimentoSerializer(estoque_estabelecimento, many=True)

        return Response(print(estoque_estabelecimento))
# from django.contrib.auth import authenticate



# class autenticar(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#         else:





# ------------------------------

class buscarProfissionalPorCPF(APIView):
    def get(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(cpf = kwargs.get('cpf'))
        # print(usuario)
        profissional = Profissional.objects.get(usuario = usuario)
        # profissional = Profissional.objects.get(usuaro = usuario)
        serializer = ProfissionalListagem(profissional)
        return Response(serializer.data)

class buscarEstabelecimentoPorCNES(APIView):
    def get(self, request, *args, **kwargs):
        estabelecimento = Estabelecimento.objects.get(cnes = kwargs.get('cnes'))
        serializer = BuscarEstabelecimentoSerializer(estabelecimento)
        return Response(serializer.data)


# class buscarEstabelecimento(ListAPIView):
#     queryset = Estabelecimento.objects.all().reverse().order_by('id')
#     serializer_class = EstabelecimentoSerializer
#     pagination_class = PaginationDefault
#     filter_backends = (SearchFilter)
#     search_fields = ['cnes', 'nome', 'logradouro']


# class buscarProfissional(ListAPIView):
#     queryset = Usuario.objects.all().reverse().order_by('id')
#     serializer_class = BuscarEstabelecimentoSerializer
#     pagination_class = PaginationDefault
#     filter_backends = (SearchFilter,)
#     search_fields = ['username', 'nome', 'cpf']