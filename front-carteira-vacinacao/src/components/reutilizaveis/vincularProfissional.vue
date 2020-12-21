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
                                <div class="col-md-6 col-sm-12">
                                    
                                    <div class="form-group">
                                        <label class="col-form-label">Digite o CPF do profissional</label>
                                        <div class="">
                                            <div class="input-group">
                                                <input type="text" v-model="buscaProfissional" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="basic-addon2">
                                                <div class="input-group-append">
                                                    <button class="btn btn-outline-primary waves-effect waves-light" @click="buscarProfissional" type="button"><i class="fa fa-search"></i> Pesquisar</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="col-md-6 col-sm-12">
                                    <div class="form-group">
                                        <label class="col-form-label">Digite o CNES do estabelecimento que quer vincular o profisisonal</label>
                                        <div class="">
                                            <div class="input-group">
                                                <input v-model="buscaEstabelecimento" type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="basic-addon2">
                                                <div class="input-group-append">
                                                    <button class="btn btn-outline-primary waves-effect waves-light" @click="buscarEstabelecimento" type="button"><i class="fa fa-search"></i> Pesquisar</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col">
                                    <div class="row">
                                        <div class="col-md-6 col-sm-12">
                                            <div class="card w-100" v-if="resultadoProfissionais != ''">
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
                                            <div class="card w-100"  v-if="resultadoEstabelecimento != ''">
                                                <div class="card-body border">
                                                    <ul>
                                                        <li>
                                                           <strong>Nome:</strong> {{resultadoEstabelecimento.nome}}
                                                        </li>
                                                        <li>
                                                            <strong>CNES: </strong>{{resultadoEstabelecimento.cnes}}
                                                        </li>
                                                        <li>
                                                            <strong>Logradouro:</strong> {{resultadoEstabelecimento.logradouro}}. {{resultadoEstabelecimento.municipio.Nome_Municipio}} - {{resultadoEstabelecimento.municipio.Nome_UF}}
                                                        </li>
                                                        <li>
                                                            <strong>Telefone:</strong> {{resultadoEstabelecimento.telefone}}
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                            
                                    </div>
                                </div>


                            </div>
                            <div class="col mt-5">
                                <div class="row justify-content-center" v-if="resultadoProfissionais != '' && resultadoEstabelecimento != '' ">
                                    <button class="btn btn-outline-primary" @click="vincularProfissional">
                                        Vincular Profissional ao Estabelecimento
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
            resultadoEstabelecimento: '',
            resultado: false,
            buscaEstabelecimento: '',
            buscaProfissional: ''
            // queryProfissional: 'search=',
            // queryEstabelecimento: 'search='
        }
    },
    methods: {
        buscarProfissional: function(){
            // this.queryProfissional += this.buscaProfissional
            // console.log(this.queryProfissional)
            serviceProfissionais.getProfissionalPorCPF(this.buscaProfissional).then(resposta =>{
                console.log(resposta.data)
                this.resultadoProfissionais = resposta.data
            })
            this.resultado = true

            // this.queryProfissional ='search='
        },
        buscarEstabelecimento: function(){

            // this.queryEstabelecimento += this.buscaEstabelecimento
            // console.log(this.queryEstabelecimento)
            serviceProfissionais.getEstabelecimentoPorCNES(this.buscaEstabelecimento).then(resposta =>{
                console.log(resposta.data)
                this.resultadoEstabelecimento = resposta.data
            })

            this.resultado = true
        },
        vincularProfissional: function(){
            serviceProfissionais.vincularProfissional(this.resultadoProfissionais.usuario.id, this.resultadoEstabelecimento.id).then(resposta =>{
                console.log(resposta.data)
                
            })
        }
    },


}
</script>