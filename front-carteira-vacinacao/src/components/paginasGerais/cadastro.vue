<template>
    <div id="estrutura">
        <!-- <div class="">
            <div class="card">
                <div class="card-body">                        
                    <img src="" alt="" srcset="">

                    <form action="">
                        <div class="form-group">
                            <label class="" for="exampleInputEmail1">Nome:</label>
                            <input type="email" class="form-control"  placeholder="">
                        </div>
                        <div class="form-group">

                        </div>

                        <div class="form-group">
                            <label class="w-100 text-left" for="exampleInputEmail1">CPF:</label>
                            <input type="text" class="form-control" id="inputCPF" v-model="novo_usuario.cpf" placeholder="">
                        </div>


                    </form>


                </div>
            </div>
        </div> -->

        <div class="col-lg-5 col-md-6 col-sm-12">

            <div class="card-box">
                <h4 class="header-title m-t-0">Cadastro de Usuário</h4>
                <p class="text-muted font-14 m-b-20">
                    Preencha os campos e clique no botão de <i>Salvar</i> para criar um usuário. Para retornar a página Inicial clique em cancelar.
                </p>

                <form action="#" novalidate="">
                    <div class="form-group">
                        <label for="inputNome" class="w-100 text-left">Nome<span class="text-danger">*</span></label>
                        <input type="text" parsley-trigger="change" required placeholder="Escreva seu nome" class="form-control" id="inputNome" v-model="novo_usuario.nome">
                    </div>
                    <div class="form-group">
                        <label for="inputCPF" class="w-100 text-left">CPF<span class="text-danger">*</span></label>
                        <input type="text"  parsley-trigger="change" required placeholder="Digite seu CPF" class="form-control" id="inputCPF" v-model="novo_usuario.cpf">
                    </div>
                    <div class="form-group">
                        <label class="w-100 text-left" for="exampleInputEmail1">Escolha o tipo de usuario:</label>
                        <select class="form-control" v-model="novo_usuario.tipo_usuario">
                            <option value="1">Coordenador do SUS</option>
                            <option value="3">Paciente do SUS</option>
                        </select>

                    </div>
                    <div class="form-group">
                        <label for="inputUsername" class="w-100 text-left">Nome de Usuario<span class="text-danger">*</span></label>
                        <input type="text"  parsley-trigger="change" required placeholder="Digite seu nome de usuário" class="form-control" id="inputUsername" v-model="novo_usuario.username">
                    </div>
                    <div class="form-group">
                        <label for="inputPassword" class="w-100 text-left">Senha<span class="text-danger">*</span></label>
                        <input type="password" placeholder="Password" id="inputPassword" v-model="novo_usuario.password" required class="form-control">
                    </div>

                    <div class="form-group justify-content-between text-right m-b-0">

                        <router-link class="btn btn-secondary waves-effect waves-light" to="paginaInicial">Cancelar</router-link>

                        <button class="btn btn-primary waves-effect waves-light ml-2" type="submit" @click="cadastrarUsuario">
                            Salvar
                        </button>
                    </div>

                </form>
            </div> <!-- end card-box -->
        </div>
    </div>
</template>


<script>
import serviceCadastro from '@/service/serviceCadastro'
export default {
    name: 'Cadastro',
    data() {
        return {
            novo_usuario: {
                nome: '',
                tipo_user: null,
                cpf: '',
                username: '',
                password: ''
            }
        }
    },
    methods: {
        cadastrarUsuario:function(){

            serviceCadastro.cadastrarUsuario(this.novo_usuario).then(resposta=>{
                    console.log(resposta.status)
                    console.log(resposta.data)
                    this.$swal.fire(
                        'Cadastrado',
                        'Você foi cadastrado, por favor faça login',
                        'success'
                    ).then(
                        this.$router.push('login')
                    )
                
            })
        }
    },
}
</script>