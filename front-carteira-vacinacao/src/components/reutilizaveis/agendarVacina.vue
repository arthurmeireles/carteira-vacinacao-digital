<template>
    <div id="wrapper" class="">
        <div class="content mt-5">
            <div class="container-fluid">
                <div class="row justify-content-center">
                    <div class="col-lg-12">
                        <div class="card-box">
                            <div class="row">
                                <div class="col ">
                                    <h4 class="m-t-0 header-title">Modulo Usuário - Marcar um agendamento</h4>
                                    <p class="text-muted font-14 m-b-20">
                                        Busque uma vacina, selecione um estabelecimento e agende sua aplicação
                                    </p>
                                </div>
                            </div>

                            <div class="row">
                                <div class="col-md-6 col-sm-12">
                                    <div class="form-group">
                                        <label class="col-form-label">Digite a vacina que busca</label>
                                        <div class="">
                                            <div class="input-group">
                                                <input v-model="palavraChave" type="text" class="form-control" placeholder="Buscar Vacina" aria-label="Recipient's username" aria-describedby="basic-addon2">
                                                <div class="input-group-append">
                                                    <button class="btn btn-outline-primary waves-effect waves-light" @click="buscarVacina" type="button"><i class="fa fa-search"></i> Pesquisar</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="col-md-6 col-sm-12">
                                    <h3 class="header-title">Resultados</h3>

                                        <div class="col-md-12 col-sm-12" v-if="resultados != ''">
                                            <div class="card w-100"  v-if="resultados != ''">
                                                <div class="card-body border">
                                                    <ul class="mb-0">
                                                        <li v-for="resultado in resultados" :key="resultado.key">
                                                            <a type="button" @click="selecionaVacina(resultado)" >
                                                                <h4 class="mb-0"><strong>{{resultado.nome}}</strong> </h4>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                    <ul class="mb-0">
                                                        <li v-for="resultado in resultadosEstabelecimentos" :key="resultado.key">
                                                            <a type="button" @click="selecionaEstabelecimento(resultado)" >
                                                                <h4 class="mb-0"><strong>{{resultado.nome}}</strong> </h4>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
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
import serviceVacinas from '@/service/serviceVacinas'
export default {
    name: 'agendarVacina',
    data() {
        return {
            vacinaEscolhida: '',
            resultados: [],
            resultadosEstabelecimentos: [],
            query: 'search=',
            palavraChave: ''
        }
    },
    methods: {
        buscarVacina: function(){
            this.query +=this.palavraChave
            console.log(this.query)
            serviceVacinas.buscarVacina(this.query).then(resposta =>{
                console.log(resposta.data.results)
                this.resultados = resposta.data.results
                this.query = 'search='

            })
        },
        selecionaVacina: function (vacina){
            this.vacinaEscolhida = vacina

            serviceVacinas.getVacinaEstabelecimento(this.vacinaEscolhida.id).then(resposta =>{
                this.resultados = []
                console.log(resposta.data)
            })
        },
        selecionaEstabelecimento: function(estabelecimento) {
            console.log(estabelecimento)
            console.log(this.vacinaEscolhida)
            
        }
    },
}
</script>