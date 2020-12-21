from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *

# ------------------------------------------------------------------------------

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class RegistroSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

# ------------------------------------------------------------------------------


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = '__all__'

# ------------------ PROFISSIONAL SERIALIZER ------------------

class ProfissionalSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(many=False, read_only=True)
    class Meta:
        model = Profissional
        fields = '__all__'
class ProfissionalListagem (serializers.ModelSerializer):
    estabelecimento = EstabelecimentoSerializer()
    usuario = UsuarioSerializer()
    class Meta:
        model = Profissional
        fields = '__all__'

class BuscaProfissionalSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    class Meta:
        model = Profissional
        fields = ['id', 'username', 'email', 'nome', 'tipo_usuario']

class BuscarEstabelecimentoSerializer(serializers.ModelSerializer):
    municipio = MunicipioSerializer()
    class Meta:
        model = Estabelecimento
        fields = ['id', 'cnes', 'nome', 'logradouro', 'municipio', 'telefone']

# ------------------------------------------------------------------------------

class PacienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(many=False, read_only=True)
    class Meta:
        model = Paciente
        fields = '__all__'

class CarteiraVacinacaoSerializer(serializers.ModelSerializer):

    paciente = PacienteSerializer(many=False, read_only=True)
    usuario_id = serializers.CharField(write_only=True, required=True)
    def create(self, validated_data):
        print(validated_data)
        paciente = Paciente.objects.get(usuario_id = validated_data.get('usuario_id'))
        
        return CarteiraVacinacao.objects.create(paciente = paciente)
    class Meta:
        model = CarteiraVacinacao
        fields = '__all__'

# ------------------- AGENDAMENTOS ------------------------

class AgendamentoCriacao(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'
class AgendamentoListagem(serializers.ModelSerializer):
    paciente = PacienteSerializer()
    estabelecimento = EstabelecimentoSerializer()
    class Meta:
        model = Agendamento
        fields = '__all__'
class EditarAgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['hora','data', 'aberto']
        

# ------------------------------------------------------------------------------
class CoordenadorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(many=False, read_only=True)
    class Meta:
        model = Coordenador
        fields = '__all__'
# ------------------------------------------------------------------------------

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = '__all__'



class BuscaVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = ['id', 'nome']

class EditarVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = ['hora','data', 'aberto']



# ------------------------------------------------------------------------------

class AplicacaoSerializer(serializers.ModelSerializer):
    carteiraVacinacao = CarteiraVacinacaoSerializer()
    estabelecimento = EstabelecimentoSerializer()
    profissional = ProfissionalSerializer()
    vacina = VacinaSerializer()
    class Meta:
        model = Aplicacao
        fields = '__all__'

class AplicacaoCriacaoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Aplicacao
        fields = '__all__'
# ------------------------------------------------------------------------------

class VacinaEstabelecimentoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Vacina_Estabelecimento
        fields = '__all__'

class ListaVacinaEstabelecimentoSerializer (serializers.ModelSerializer):
    estabelecimento = EstabelecimentoSerializer()
    vacina = VacinaSerializer()
    class Meta: 
        model = Vacina_Estabelecimento
        fields = '__all__'
