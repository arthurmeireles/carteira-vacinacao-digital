<template>
    <div id="wrapper" class="">
        <div class="content mt-5">
            <div class="container-fluid">
                <div class="row justify-content-center">
                    <div class="col-md-5 col-sm-12">
                        <div class="card-box">
                            <h4 class="header-title m-t-0">Cadastro de Coordenador do SUS</h4>
                            <p class="text-muted font-14 m-b-20">
                                Preencha os campos e clique no botão de <i>Salvar</i> para criar um usuário. Para retornar a página Inicial clique em cancelar.
                            </p>

                            <form action="#" novalidate="">
                                <div class="form-group">
                                    <label for="inputNome" class="w-100 text-left">Nome<span class="text-danger">*</span></label>
                                    <input type="text" parsley-trigger="change" required placeholder="Escreva seu nome" class="form-control" id="inputNome" v-model="novo_user_coordenador.nome">
                                </div>
                                <div class="form-group">
                                    <label for="inputCPF" class="w-100 text-left">CPF<span class="text-danger">*</span></label>
                                    <input type="text"  parsley-trigger="change" required placeholder="Digite seu CPF" class="form-control" id="inputCPF" v-model="novo_user_coordenador.cpf">
                                </div>

                                <div class="form-group">
                                    <label for="inputUsername" class="w-100 text-left">Nome de Usuario<span class="text-danger">*</span></label>
                                    <input type="text"  parsley-trigger="change" required placeholder="Digite seu nome de usuário" class="form-control" id="inputUsername" v-model="novo_user_coordenador.username">
                                </div>
                                <div class="form-group">
                                    <label for="inputPassword" class="w-100 text-left">Senha<span class="text-danger">*</span></label>
                                    <input type="password" placeholder="Password" id="inputPassword" v-model="novo_user_coordenador.password" required class="form-control">
                                </div>

                                <div class="form-group justify-content-between text-right m-b-0">

                                    <router-link class="btn btn-secondary waves-effect waves-light" to="paginaInicial">Cancelar</router-link>

                                    <button class="btn btn-primary waves-effect waves-light ml-2" @click="cadastrarUsuarioCoordenador">
                                        Salvar
                                    </button>
                                </div>

                            </form>
                        </div> <!-- end card-box -->
                    </div>
                    <div class="col-md-5 col-sm-12">
                        <div class="card-box">
                            <h4 class="header-title m-t-0">Cadastro de Profissional de Saúde</h4>
                            <p class="text-muted font-14 m-b-20">
                                Preencha os campos e clique no botão de <i>Salvar</i> para criar um usuário. Para retornar a página Inicial clique em cancelar.
                            </p>

                            <form action="#" novalidate="">
                                <div class="form-group">
                                    <label for="inputNome" class="w-100 text-left">Nome<span class="text-danger">*</span></label>
                                    <input type="text" parsley-trigger="change" required placeholder="Escreva seu nome" class="form-control" id="inputNome" v-model="novo_user_profissional.nome">
                                </div>
                                <div class="form-group">
                                    <label for="inputCPF" class="w-100 text-left">CPF<span class="text-danger">*</span></label>
                                    <input type="text"  parsley-trigger="change" required placeholder="Digite seu CPF" class="form-control" id="inputCPF" v-model="novo_user_profissional.cpf">
                                </div>

                                <div class="form-group">
                                    <label for="inputUsername" class="w-100 text-left">Nome de Usuario<span class="text-danger">*</span></label>
                                    <input type="text"  parsley-trigger="change" required placeholder="Digite seu nome de usuário" class="form-control" id="inputUsername" v-model="novo_user_profissional.username">
                                </div>
                                <div class="form-group">
                                    <label for="inputPassword" class="w-100 text-left">Senha<span class="text-danger">*</span></label>
                                    <input type="password" placeholder="Password" id="inputPassword" v-model="novo_user_profissional.password" required class="form-control">
                                </div>

                                <div class="form-group justify-content-between text-right m-b-0">

                                    <router-link class="btn btn-secondary waves-effect waves-light" to="paginaInicial">Cancelar</router-link>

                                    <button class="btn btn-primary waves-effect waves-light ml-2" @click="cadastrarUsuarioProfissional">
                                        Salvar
                                    </button>
                                </div>

                            </form>
                        </div> <!-- end card-box -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import serviceCadastro from '@/service/serviceCadastro'

export default {
    name: 'Usuarios',
    data() {
        return {
            novo_user_coordenador: {
                nome: '',
                tipo_usuario: 1,
                cpf: '',
                username: '',
                password: ''
            },
            novo_user_profissional: {
                nome: '',
                tipo_usuario: 2,
                cpf: '',
                username: '',
                password: ''
            }
        }
    },
    methods: {
        cadastrarUsuarioCoordenador:function(){
            serviceCadastro.cadastrarUsuario(this.novo_user_coordenador).then(resposta=>{
                if(resposta.status == 201 ){
                    this.$swal.fire(
                        'Cadastrado',
                        'Você foi cadastrado, por favor faça login',
                        'success'
                    )
                    this.novo_user_coordenador.nome = ''
                    this.novo_user_coordenador.cpf = ''
                    this.novo_user_coordenador.username = ''
                    this.novo_user_coordenador.password = ''
                }
            })
        },
        cadastrarUsuarioProfissional:function(){
            serviceCadastro.cadastrarUsuario(this.novo_user_profissional).then(resposta=>{
                if(resposta.status == 201 ){
                    this.$swal.fire(
                        'Cadastrado',
                        'Você foi cadastrado, por favor faça login',
                        'success'
                    )
                    this.novo_user_profissional.nome = ''
                    this.novo_user_profissional.cpf = ''
                    this.novo_user_profissional.username = ''
                    this.novo_user_profissional.password = ''
                }
            })
        },

    },
}
</script>