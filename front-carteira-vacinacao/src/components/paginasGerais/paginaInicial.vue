<template>
    <div>
        <nav class="position-stick">
            <router-link class="btn btn-primary mt-3 mr-3 float-right" to="Cadastro">Registre-se</router-link>
        </nav>

        <header class="meubg-primary">
            <div class="container my-auto d-block h-100">

                <div class="row h-100 align-items-center">
                    <div class="col-md-6 col-sm-12">
                        <h1 class="display-4 font-weight-bold text-white"> Carteira Digital de Vacinação</h1>
                        <h2 class="text-grey font-weight-light"> Sistema de agendamento e gerenciamento de vacinação </h2>
                        <div class="col row mt-3">
                            <!-- <button type="button" class="btn btn-primary">Cadastrar</button> -->
                            <router-link class="btn btn-outline-primary" to="login">Entrar</router-link>
                        </div>
                    </div>

                </div>
            </div>

        </header>
    </div>
</template>

<style scoped>
@media(max-width: 540px){
    #mobile-some{
        display: none;
    }
}
.meubg-primary {
    height: 100vh;
}

</style>
<script>
export default {
    
}
</script>