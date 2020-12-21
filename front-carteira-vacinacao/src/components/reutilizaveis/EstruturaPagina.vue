<template>
    <div id="estrutura">        
        <Navbar/>


        <router-view :usuario="usuario"></router-view> 

    </div>
</template>


<style scoped>
    #estrutura{
        flex-direction: column;
    }
</style>
<script>
import Navbar from './Navbar'


export default {
    name: 'EstruturaPagina',
        components: {
            Navbar
        },
    data(){
        return{
            usuario: ''
        }
    },
    mounted() {
        // serviceUsuario.getUsuarioLogado().then(resposta=>{
        //     if(resposta.status == 200){
        //         this.usuario = resposta.data

        //         localStorage.setItem('usuarioId', this.usuario.id)
        //     }
        // }).catch(
        //     (error) =>{
        //         this.$router.push({name: 'login'})
        //         console.log(error)
        // })
    },

}
</script>