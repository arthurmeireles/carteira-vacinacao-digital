<template>
    <div id="estrutura">

        <router-view :usuario="usuario"></router-view> 

    </div>
</template>



<script>
export default {
    name: 'EstruturaPagina',
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