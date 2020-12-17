from django.db import models
from django.contrib.auth.models import User, AbstractUser




# Create your models here.

# Essa classe ta herdando os dados do AbstractUser
class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        (1, 'Coordenador'),
        (2, 'Profissional'),
        (3, 'Paciente')
    )
    nome = models.CharField(max_length=1000, blank=True)
    tipo_usuario = models.PositiveSmallIntegerField(choices=TIPO_USUARIO_CHOICES, blank=True)
    cpf = models.CharField(max_length=11, blank=True)

class Municipio(models.Model):
    UF = models.IntegerField()
    Nome_UF = models.CharField(max_length=1000, blank=True)
    Codigo_Municipio = models.CharField(max_length=100)
    Nome_Municipio = models.CharField(max_length=1000)
    

class Vacina(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField(null=True)
         
class Estabelecimento(models.Model):
    cnes = models.CharField(max_length=12, verbose_name=u'Código CNES', unique=True)
    nome = models.CharField(max_length=60)
    logradouro = models.CharField(max_length=60, verbose_name=u'Logradouro', null=True, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9, verbose_name=u'CEP', null=True, blank=True)
    telefone = models.CharField(max_length=40, verbose_name=u'Telefone', null=True, blank=True)
    celular = models.CharField(max_length=40, verbose_name=u'Celular', null=True, blank=True)
    email = models.CharField(max_length=100, verbose_name=u'Email', null=True, blank=True)
    complemento = models.CharField(max_length=255, verbose_name=u'Complemento', null=True, blank=True)
    bairro = models.CharField(max_length=60, verbose_name=u'Bairro', null=True, blank=True)
    vacinas = models.ManyToManyField(Vacina, verbose_name=u"Vacinas do Estabelecimento")

class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='paciente_usuario')

class CarteiraVacinacao(models.Model):
    usuario = models.OneToOneField(Paciente, on_delete=models.CASCADE,  related_name='paciente_carteira')

class Aplicacao(models.Model):
    vacina = models.ForeignKey(Vacina, on_delete=models.SET_NULL, null=True, related_name='vacina_carteira')
    carteiraVacinacao = models.ForeignKey(CarteiraVacinacao, on_delete=models.SET_NULL, null=True)
    data_aplicacao = models.DateField(null=True)

class Coordenador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='coordenador_usuario')


class Profissional(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='profissional_usuario')
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.SET_NULL, null=True, blank=True)



class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True)