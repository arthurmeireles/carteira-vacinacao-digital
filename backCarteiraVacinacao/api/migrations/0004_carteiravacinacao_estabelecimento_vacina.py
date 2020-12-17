# Generated by Django 3.1.4 on 2020-12-17 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_municipio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnes', models.CharField(max_length=12, unique=True, verbose_name='Código CNES')),
                ('nome', models.CharField(max_length=60)),
                ('logradouro', models.CharField(blank=True, max_length=60, null=True, verbose_name='Logradouro')),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('telefone', models.CharField(blank=True, max_length=40, null=True, verbose_name='Telefone')),
                ('celular', models.CharField(blank=True, max_length=40, null=True, verbose_name='Celular')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=60, null=True, verbose_name='Bairro')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.municipio')),
                ('vacina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vacina_estabelecimento', to='api.vacina')),
            ],
        ),
        migrations.CreateModel(
            name='CarteiraVacinacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_carteira', to='api.paciente')),
                ('vacina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vacina_carteira', to='api.vacina')),
            ],
        ),
    ]
