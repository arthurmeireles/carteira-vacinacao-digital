<template>
    <div id="wrapper">
        <div class="content mt-5">
            <div class="content pt-5">
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-lg-6">
                            <div class="card-box">
                                <h4 class="m-t-0 header-title">Modulo Paciente - Carteira de Vacinação</h4>
                                <p class="text-muted font-14 m-b-20">
                                    Todos as aplicações realizadas no Paciente
                                </p>
                        
                                <table class="table table-hover">
                                    <thead>
                                        <tr>
                                            <th>Data da Aplicacao</th>
                                            <th>Estabelecimento</th>
                                            <th>Vacina</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="aplicacao in vacinasAplicadasPaciente" :key="aplicacao.id">
                                            <td>{{aplicacao.data_aplicacao}}</td>
                                            <td>{{aplicacao.estabelecimento.nome}}</td>
                                            <td>{{aplicacao.vacina.nome}}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        
                        </div>

                        <div class="col-lg-6 col-md-12 col-sm-12">
                            <div class="card-box">
                                <div class="row">
                                    <div class="col ">
                                        <h4 class="m-t-0 header-title">Modulo Paciente - Lista de Agendamentos do Paciente</h4>
                                        <p class="text-muted font-14 m-b-20">
                                            Todos os agendamentos que o paciente está vinculado
                                        </p>
                                    </div>
                                    <div class="col">
                                        <div class="d-flex justify-content-end">
                                            <button type="button" class="btn btn-outline-primary ml-auto" data-toggle="modal" data-target="#modalAgendar">Agendar Vacina</button>
                                        </div>
                                    </div>
                                </div>
                                <div class="modal fade" id="modalAgendar" tabindex="-1" role="dialog" aria-labelledby="modalAgendar" aria-hidden="true">
                                    <div class="modal-dialog modal-dialog-centered" role="document">
                                        <div class="modal-content">
                                            <div class="modal-header">
                                                <h4 class="modal-title" id="exampleModalLongTitle">Adicionar Agendamento</h4>
                                                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                    <span aria-hidden="true">&times;</span>
                                                </button>
                                            </div>
                                            <div class="modal-body">
                                                
                                                <form action="">
                                                    <div class="form-group">
                                                        <label for="inputData">Data do agendamento</label>
                                                        <div class="input-group">
                                                            <input v-model="novo_agendamento.data" type="text" class="form-control" placeholder="mm/dd/yyyy" id="inputData">
                                                            <div class="input-group-append">
                                                                <span class="input-group-text"><i class="ion-calendar"></i></span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label for="inputData">Hora do agendamento</label>
                                                        <div class="input-group">
                                                            <input v-model="novo_agendamento.hora" type="text" class="form-control" placeholder="hh:mm" id="inputHora">
                                                            <div class="input-group-append">
                                                                <span class="input-group-text"><i class="mdi mdi-calendar-clock"></i></span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </form>
                                            </div>
                                            <div class="modal-footer">
                                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                                                <button type="button" class="btn btn-primary" @click="adicionarAgendamento">Adicionar</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                        
                                <table class="table table-hover">
                                    <thead>
                                        <tr>
                                            <th>Data</th>
                                            <th>Hora</th>
                                            <th>Estabelecimento</th>
                                            <th>Vacina</th>
                                            <th>Opções</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="agendamento in agendamentosPaciente" :key="agendamento.id">
                                            <td>{{agendamento.data}}</td>
                                            <td>{{agendamento.hora}}</td>
                                            <td>{{agendamento.estabelecimento.nome}}</td>
                                            <td v-if="agendamento.paciente != null">{{agendamento.paciente.usuario.nome}}</td>
                                            <td v-else>Não possui</td>
                                            <td>
                                                <button class="btn btn-icon waves-effect waves-light btn-danger mr-1" @click="cancelarAgendamento(agendamento.id)">
                                                    <i class="fa fa-remove"></i>
                                                </button>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        
                        </div>
                        <div class="col-lg-6 col-md-12 col-sm-12">
                            <div class="card-box">
                                <div class="row">
                                    <div class="col ">
                                        <h4 class="m-t-0 header-title">Modulo Profissional - Lista de Agendamentos Marcados</h4>
                                        <p class="text-muted font-14 m-b-20">
                                            Todos os agendamentos que tem um paciente
                                        </p>
                                    </div>
                                </div>

                        
                                <table class="table table-hover">
                                    <thead>
                                        <tr>
                                            <th>Data</th>
                                            <th>Hora</th>
                                            <th>Estabelecimento</th>
                                            <th>Paciente</th>
                                            <th>Status</th>
                                            <th>Opções</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="agendamento in agendamentosMarcado" :key="agendamento.id">
                                            <td>{{agendamento.data}}</td>
                                            <td>{{agendamento.hora}}</td>
                                            <td>{{agendamento.estabelecimento.nome}}</td>
                                            <td v-if="agendamento.paciente != null">{{agendamento.paciente.usuario.nome}}</td>
                                            <td v-else>Não possui</td>

                                            <td v-if="agendamento.paciente != null">Preenchido</td>
                                            <td v-else>Disponivel</td>
                                            <td>
                                                <button class="btn btn-icon waves-effect waves-light btn-success mr-1">
                                                    <i class="fa fa-check"></i>
                                                </button>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        
                        </div>
                        <div class="col-lg-6 col-md-12 col-sm-12">
                            <div class="card-box">
                                <div class="row">
                                    <div class="col ">
                                        <h4 class="m-t-0 header-title">Modulo Profissional -Lista de Agendamentos</h4>
                                        <p class="text-muted font-14 m-b-20">
                                            Todos os agendamentos
                                        </p>
                                    </div>
                                    <div class="col">
                                        <div class="d-flex justify-content-end">
                                            <button type="button" class="btn btn-outline-primary ml-auto" data-toggle="modal" data-target="#modalAdcAgendamento">Adicionar Agendamento</button>
                                        </div>
                                    </div>

                                    <div class="modal fade" id="modalAdcAgendamento" tabindex="-1" role="dialog" aria-labelledby="modalAdcAgendamento" aria-hidden="true">
                                        <div class="modal-dialog modal-dialog-centered" role="document">
                                            <div class="modal-content">
                                                <div class="modal-header">
                                                    <h4 class="modal-title" id="exampleModalLongTitle">Adicionar Agendamento</h4>
                                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                        <span aria-hidden="true">&times;</span>
                                                    </button>
                                                </div>
                                                <div class="modal-body">
                                                    
                                                    <form action="">
                                                        <div class="form-group">
                                                            <label for="inputData">Data do agendamento</label>
                                                            <div class="input-group">
                                                                <input v-model="novo_agendamento.data" type="text" class="form-control" placeholder="mm/dd/yyyy" id="inputData">
                                                                <div class="input-group-append">
                                                                    <span class="input-group-text"><i class="ion-calendar"></i></span>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="form-group">
                                                            <label for="inputData">Hora do agendamento</label>
                                                            <div class="input-group">
                                                                <input v-model="novo_agendamento.hora" type="text" class="form-control" placeholder="hh:mm" id="inputHora">
                                                                <div class="input-group-append">
                                                                    <span class="input-group-text"><i class="mdi mdi-calendar-clock"></i></span>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </form>
                                                </div>
                                                <div class="modal-footer">
                                                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                                                    <button type="button" class="btn btn-primary" @click="adicionarAgendamento">Adicionar</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                        
                                <table class="table table-hover">
                                    <thead>
                                        <tr>
                                            <th>Data</th>
                                            <th>Hora</th>
                                            <th>Estabelecimento</th>
                                            <th>Paciente</th>
                                            <th>Status</th>
                                            <th>Opções</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="agendamento in agendamentosDisponiveis" :key="agendamento.id">
                                            <td>{{agendamento.data}}</td>
                                            <td>{{agendamento.hora}}</td>
                                            <td>{{agendamento.estabelecimento.nome}}</td>
                                            <td v-if="agendamento.paciente != null">{{agendamento.paciente.usuario.nome}}</td>
                                            <td v-else>Não possui</td>

                                            <td v-if="agendamento.paciente != null">Preenchido</td>
                                            <td v-else>Disponivel</td>
                                            <td>
                                                <button class="btn btn-icon waves-effect waves-light btn-warning mr-1">
                                                    <i class="ion-edit"></i>
                                                </button>
                                                <button class="btn btn-icon waves-effect waves-light btn-danger mr-1" @click="deletarAgendamento(agendamento.id)">
                                                    <i class="fa fa-remove"></i>
                                                </button>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        
                        </div>
                        <div class="col-lg-6">

                            <div class="card-box">
                                <div class="row">
                                    <div class="col ">

                                        <h4 class="m-t-0 header-title">Modulo Coordenador - Vacinas</h4>
                                        <p class="text-muted font-14 m-b-20">
                                            Listagem de vacinas cadastradas 
                                        </p>
                                    </div>
                                    <div class="col ">
                                        <div class="d-flex justify-content-end">
                                            <button type="button" class="btn btn-outline-primary ml-auto" data-toggle="modal" data-target="#modalAdcVacina">Adicionar Vacina</button>
                                        </div>
                                    </div>
                                    <div class="modal fade" id="modalAdcVacina" tabindex="-1" role="dialog" aria-labelledby="modalAdcAgendamento" aria-hidden="true">
                                        <div class="modal-dialog modal-dialog-centered" role="document">
                                            <div class="modal-content">
                                                <div class="modal-header">
                                                    <h4 class="modal-title" id="exampleModalLongTitle">Adicionar Vacina</h4>
                                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                        <span aria-hidden="true">&times;</span>
                                                    </button>
                                                </div>
                                                <div class="modal-body">
                                                    
                                                    <form action="">
                                                        <div class="form-group">
                                                            <label for="userName">Nome da Vacina<span class="text-danger">*</span></label>
                                                            <input  v-model="nova_vacina.nome" type="text" name="nick" parsley-trigger="change" required placeholder="Nome da Vacina" class="form-control" id="userName">
                                                        </div>
                                                    </form>
                                                </div>
                                                <div class="modal-footer">
                                                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                                                    <button type="button" class="btn btn-primary" @click="adicionarVacina">Adicionar</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                        
                                <table class="table table-hover">
                                    <thead>
                                        <tr>
                                            <th>Nome</th>
                                            <th>Opções</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="vacina in vacinas" :key="vacina.id">
                                            <td>{{vacina.nome}}</td>
        
                                            <td>
                                                <button class="btn btn-icon waves-effect waves-light btn-warning mr-1">
                                                    <i class="ion-edit"></i>
                                                </button>

                                                <button class="btn btn-icon waves-effect waves-light btn-danger mr-1" @click="deletarVacina(vacina.id)">
                                                    <i class="fa fa-remove"></i>
                                                </button>

                                            </td> 
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>

    </div>

</template>


<script>
import serviceAgendamentos from "@/service/serviceAgendamentos"
import serviceVacinas from "@/service/serviceVacinas"
import serviceProfissionais from "@/service/serviceProfissionais"


export default {
    name: 'Dashboard',
    data() {
        return {
            
            vincular_profissional_estabelecimento:{
                usuario_id: '',
                estabelecimento_id: ''
            },
            nova_vacina: {
                nome: ''
            },
            profissionais: [],
            agendamentos: [],
            agendamentosDisponiveis: [],
            agendamentosMarcado: [],
            agendamentosPaciente: [],
            vacinas: [],
            vacinasAplicadasPaciente: [],
            usuarioPaciente: {
                id: 1
            },
            usuarioProfissional: {
                id: 1
            },
            usuarioCoordenador: {
                id: 1
            },
            novo_agendamento: {
                data: '',
                hora: '',
                estabelecimento: 1,
                profissional: 1
            }
        }
    },

    methods: {
        adicionarAgendamento: function(){
            serviceAgendamentos.adicionarAgendamento(this.novo_agendamento).then(resposta=>{
                console.log(resposta.status)
                console.log(resposta.data)
                if(resposta.status == 201){
                    this.$swal.fire(
                        'Cadastrado',
                        'Agendamento Cadastrado com sussesso',
                        'success'
                    )
                }
            })
        },
        adicionarVacina:function(){
            serviceVacinas.adicionarVacina(this.nova_vacina).then(resposta=>{
                if(resposta.status == 201){
                    console.log(resposta.status)
                    console.log(resposta.data)
                    this.$swal.fire(
                        'Cadastrado',
                        'Agendamento Cadastrado com sussesso',
                        'success'
                    ).then(location.reload)
                }
            })
        },
        cancelarAgendamento: function(agendamentoId){
            serviceAgendamentos.cancelarAgendamento(this.usuario.id, agendamentoId).then(resposta=>{
                console.log(resposta.data)
            })
        },
        deletarVacina: function(vacina){
            serviceVacinas.deletarVacina(vacina).then(resposta=>{
                console.log(resposta.data)
                if(resposta.status == 200){
                    this.$swal.fire(
                        'Cadastrado',
                        'Agendamento Cadastrado com sussesso',
                        'success'
                    )
                }
            })
        },
        deletarAgendamento: function(agendamento){
            serviceAgendamentos.deletarAgendamento(agendamento).then(resposta=>{
                console.log(resposta.data)
                if(resposta.status == 200){
                    this.$swal.fire(
                        'Deletado',
                        'Agendamento DELETADO com sussesso',
                        'success'
                    )
                }
            })
        },
        iniciarFrontGeral:function(){
            serviceVacinas.getVacinas().then(resposta =>{
                this.vacinas = resposta.data
            })
        },
        iniciarFrontPaciente:function(){
            serviceAgendamentos.getAgendamentos().then(resposta =>{
                this.agendamentos = resposta.data
            })
            serviceAgendamentos.getAgendamentosPaciente(this.usuario.id).then(resposta=>{
                this.agendamentosPaciente = resposta.data
                console.log(resposta.data)
            })
            serviceVacinas.getAplicacoesUsuario(this.usuario.id).then(resposta =>{
                this.vacinasAplicadasPaciente = resposta.data
            })
        },
        iniciarFrontProfissional: function(){
            // Incluir aqui um id do estabelecimento e filtrar por isso
            serviceAgendamentos.getAgendamentosMarcados().then(resposta =>{
                this.agendamentosMarcado = resposta.data
            })
            // Incluir aqui um id do estabelecimento e filtrar por isso
            serviceAgendamentos.getAgendamentosDisponiveis().then(resposta =>{
                this.agendamentosDisponiveis = resposta.data
            })
        },
        iniciaFrontCoordenador:function(){
            serviceProfissionais.getProfissionais().then(resposta=>{
                this.profissionais = resposta.data
            })
        }
    },
    mounted() {
        
        // quando finalizar, fazer uma comparação com tipo de usuario retornado do login e filtrar
        // this.iniciarFrontGeral
        // this.iniciarFrontPaciente
        // this.iniciarFrontProfissional
        // this.iniciaFrontCoordenador
            serviceVacinas.getVacinas().then(resposta =>{
                this.vacinas = resposta.data
            })
            serviceProfissionais.getProfissionais().then(resposta=>{
                this.profissionais = resposta.data
            })
                        // Incluir aqui um id do estabelecimento e filtrar por isso
            serviceAgendamentos.getAgendamentosMarcados().then(resposta =>{
                this.agendamentosMarcado = resposta.data
            })
            // Incluir aqui um id do estabelecimento e filtrar por isso
            serviceAgendamentos.getAgendamentosDisponiveis().then(resposta =>{
                this.agendamentosDisponiveis = resposta.data
            })
            serviceAgendamentos.getAgendamentos().then(resposta =>{
                this.agendamentos = resposta.data
            })
            serviceAgendamentos.getAgendamentosPaciente(1).then(resposta=>{
                this.agendamentosPaciente = resposta.data
                console.log(resposta.data)
            })
            serviceVacinas.getAplicacoesUsuario(1).then(resposta =>{
                this.vacinasAplicadasPaciente = resposta.data
            })
    },
}
</script>