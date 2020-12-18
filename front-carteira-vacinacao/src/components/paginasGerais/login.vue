<template>
    <div id="estrutura">
        <div class="col-lg-4 col-md-5 col-sm-12">
            <div class="card">
                <div class="card-body">                        
                    <img src="" alt="" srcset="">

                    <form action="">
                        <div class="form-group">
                            <label class="w-100 text-left" for="exampleInputEmail1">Nome de Usuario:</label>
                            <input type="text" class="form-control" id="inputUsername" v-model="usuario.username" placeholder="">
                        </div>
                        <div class="form-group">
                            <label class="w-100 text-left" for="exampleInputEmail1">Senha:</label>
                            <input type="password" class="form-control" id="inputPassword" v-model="usuario.password" placeholder="">
                        </div>
                    </form>

                    <div>
                        <button class="btn-primary btn float-left" type="submit" @click="logarUsuario">Enviar</button>
                    </div>

                </div>
            </div>
        </div>
    </div>


</template>

<script>
import serviceLogin from '@/service/serviceLogin'
import axios from 'axios'

export default {
    name: 'Login',
    data() {
        return {
            usuario: {
                username: '',
                password: ''
            }
        }
    },
    methods:{
        logarUsuario: function(){
            serviceLogin.login(this.usuario).then(resposta => {
                console.log(resposta.data)
                if(resposta.status == 200){
                    console.log("Logou")
                    localStorage.setItem('token', resposta.data.token)
                    axios.defaults.headers.common['Authorization'] = 'Token '+resposta.data.token ;
                    this.$router.push({name: 'paginaInicial'})
                    this.$emit('buscaUsuario')
                }
            }).catch(
                (error) =>{
                    this.$swal.fire(
                        'Oops...',
                        'Tivemos um problema, tente novamente!',
                        'error',
                    )
                    console.log(error)
                }
            )
        }

    }
}
</script>