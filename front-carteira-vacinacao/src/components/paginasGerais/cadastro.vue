<template>
    <div id="estrutura">

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
                        <label for="inputUsername" class="w-100 text-left">Nome de Usuario<span class="text-danger">*</span></label>
                        <input type="text"  parsley-trigger="change" required placeholder="Digite seu nome de usuário" class="form-control" id="inputUsername" v-model="novo_usuario.username">
                    </div>
                    <div class="form-group">
                        <label for="inputPassword" class="w-100 text-left">Senha<span class="text-danger">*</span></label>
                        <input type="password" placeholder="Password" id="inputPassword" v-model="novo_usuario.password" required class="form-control">
                    </div>

                    <div class="form-group justify-content-between text-right m-b-0">

                        <router-link class="btn btn-secondary waves-effect waves-light" to="paginaInicial">Cancelar</router-link>

                        <button class="btn btn-primary waves-effect waves-light ml-2" @click="cadastrarUsuario">
                            Salvar
                        </button>
                    </div>

                </form>
            </div> <!-- end card-box -->
        </div>
    </div>
</template>

<style scoped>
    #estrutura{
        height: 100vh;
        align-items: center;
    }
</style>
<script>
import serviceCadastro from '@/service/serviceCadastro'
export default {
    name: 'Cadastro',
    data() {
        return {
            novo_usuario: {
                nome: '',
                tipo_usuario: 3,
                cpf: '',
                username: '',
                password: ''
            },
            objeto_usuario_id: {
                usuario_id: ''
            }
        }
    },
    methods: {
        cadastrarUsuario:function(){

            serviceCadastro.cadastrarUsuario(this.novo_usuario).then(resposta=>{

                if(resposta.status == 201 ){
                    this.objeto_usuario_id.usuario_id = resposta.data.id

                    this.$swal.fire(
                        'Cadastrado',
                        'Você foi cadastrado, por favor faça login',
                        'success'
                    )
                    if(this.novo_usuario.tipo_usuario == 3){
                        serviceCadastro.criaCartaoVacinacao(this.objeto_usuario_id).then(resposta=>{
                            console.log(resposta.data)
                            console.log(resposta.status)
                        })
                    }
                }
            })
            this.$router.push('login')
        },

    },
}
</script>