<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light w-100">
    <div class="container-fluid">
        <!-- <a class="navbar-brand" href="#">Navbar</a> -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <router-link class="nav-link" to="dashboard">Página Inicial </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="usuarios">Adicionar Usuarios</router-link>
                </li>

                <li class="nav-item">
                    <router-link class="nav-link" to="agendarVacina">Agendar Vacinação</router-link>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Relatório
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                        <a class="dropdown-item" type="button" @click="baixarRelatorio">Baixar Relatório de Aplicações</a>
                    </div>
                </li>
                
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Vinculos
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                        <router-link class="dropdown-item" to="vinculoprofissionais">Vincular Profissional</router-link>
                        <router-link class="dropdown-item" to="desvincularProfissional">Desvincular Profissional</router-link>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>
</template>

<script>

import serviceAgendamentos from "@/service/serviceAgendamentos"
export default {
    methods: {
        baixarRelatorio: function(){
            serviceAgendamentos.baixarRelatorio().then(resposta=>{
                resposta.data
            })
        }
    },
}
</script>