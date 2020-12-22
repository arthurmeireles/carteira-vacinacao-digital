<template>
    <div id="estrutura">
        <div class="col-lg-4 col-md-5 col-sm-12">
            <div class="card">
                <div class="card-body">                        
                    <div class="text-center">
                        <a href="index.html" class="logo-lg"><i class="mdi mdi-radar"></i> <span>Minton</span> </a>
                    </div>

                    <form class="form-horizontal my-5">

                        <div class="form-group row">
                            <div class="col-12">
                                <div class="input-group">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text"><i class="mdi mdi-account"></i></span>
                                    </div>
                                    <input class="form-control" v-model="usuario.username" type="text" required="" placeholder="Username">
                                </div>
                            </div>
                        </div>

                        <div class="form-group row">
                            <div class="col-12">
                                <div class="input-group">
                                    <div class="input-group-prepend">
                                        <span class="input-group-text"><i class="mdi mdi-key"></i></span>
                                    </div>
                                    <input class="form-control" v-model="usuario.password" type="password" required="" placeholder="Password">
                                </div>
                            </div>
                        </div>

                        <div class="form-group text-right mt-5">
                            <div class=" d-flex justify-content-end">
                                <button class="btn btn-primary btn-custom w-md waves-effect waves-light btn-block " type="button" @click="logarUsuario">
                                    Entrar
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
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
                    localStorage.setItem('tipo_usuario', resposta.data.usuario.tipo_usuario)

                    axios.defaults.headers.common['Authorization'] = 'Token '+resposta.data.token ;
                    this.$router.push({name: 'dashboard'})

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