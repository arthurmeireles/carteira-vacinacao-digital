<template>
    <div id="wrapper" class="">
        <div class="content mt-5">
            <div class="container-fluid">
                <div class="row justify-content-center">
       
                    <div class="col-lg-12">
                        <div class="card-box">
                            <div class="row">
                                <div class="col ">
                                    <h4 class="m-t-0 header-title">Modulo Coordenador - Vincular Profissional a Estababelecimento</h4>
                                    <p class="text-muted font-14 m-b-20">
                                        Busque um profissional pelo CPF e busque um estabelecimento pelo CNES e os vincule
                                    </p>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-12 col-sm-12">
                                    
                                    <div class="form-group">
                                        <label class="col-form-label">Digite o CPF do profissional</label>
                                        <div class="">
                                            <div class="input-group">
                                                <input type="text" v-model="buscaProfissional" class="form-control" placeholder="Digite o CPF" aria-label="Recipient's username" aria-describedby="basic-addon2">
                                                <div class="input-group-append">
                                                    <button class="btn btn-outline-primary waves-effect waves-light" @click="buscarProfissional" type="button"><i class="fa fa-search"></i> Pesquisar</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                

                                <div class="col">
                                    <div class="row w-100">
                                        <div class="col-md-6 col-sm-12">
                                            <div class="card w-100 mt-3" v-if="resultadoProfissionais != ''">
                                                <div class="card-body border">

                                                    <ul>
                                                        <li>
                                                           <strong>Nome:</strong> {{resultadoProfissionais.usuario.nome}}
                                                        </li>
                                                        <li>
                                                            <strong> CPF: </strong>{{resultadoProfissionais.usuario.cpf}}
                                                        </li>
                                                        <li>
                                                            <strong>Nome de Usuário:</strong> {{resultadoProfissionais.usuario.username}}
                                                        </li>
                                                        <li>
                                                            <strong>E-mail:</strong> {{resultadoProfissionais.usuario.email}}
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>

                                        </div>                            
                                        <div class="col-md-6 col-sm-12">
                                            <div class="card w-100 mt-3"  v-if="resultadoProfissionais != ''">
                                                <div class="card-body border">
                                                    <ul>
                                                        <li>
                                                            <strong>Nome:</strong> {{resultadoProfissionais.estabelecimento.nome}}
                                                        </li>
                                                        <li>
                                                            <strong>CNES: </strong>{{resultadoProfissionais.estabelecimento.cnes}}
                                                        </li>
                                                        <li>
                                                            <strong>Logradouro:</strong> {{resultadoProfissionais.estabelecimento.logradouro}}. {{resultadoProfissionais.estabelecimento.municipio.Nome_Municipio}} - {{resultadoProfissionais.estabelecimento.municipio.Nome_UF}}
                                                        </li>
                                                        <li>
                                                            <strong>Telefone:</strong> {{resultadoProfissionais.estabelecimento.telefone}}
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        
   
                            <div class="col mt-5">
                                <div class="row justify-content-center" v-if="resultadoProfissionais != ''">
                                    <button class="btn btn-outline-primary" @click="desvincularProfissional">
                                        Desvincular Profissional do Estabelecimento
                                    </button>
                                </div>
                            </div>              
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import serviceProfissionais from '@/service/serviceProfissionais'
export default {
    name: 'VinculoProfissionais',
    data() {
        return {
            resultadoProfissionais: '',
            resultado: false,
            buscaProfissional: ''
        }
    },
    methods: {
        buscarProfissional: function(){
            serviceProfissionais.getProfissionalPorCPF(this.buscaProfissional).then(resposta =>{
                console.log(resposta.data)
                this.resultadoProfissionais = resposta.data
            })
            this.resultado = true

            // this.queryProfissional ='search='
        },
        desvincularProfissional: function(){
            serviceProfissionais.desvincularProfissional(this.resultadoProfissionais.usuario.id, this.resultadoProfissionais.estabelecimento.id).then(resposta =>{
                console.log(resposta.data)
                this.resultadoProfissionais = ''
            })
        }
    },
}
</script>