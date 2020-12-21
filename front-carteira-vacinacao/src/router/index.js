import Vue from 'vue';
import Router from 'vue-router';
import login from '../components/paginasGerais/login';
import Cadastro  from '../components/paginasGerais/cadastro';
import paginaInicial from '../components/paginasGerais/paginaInicial'
import Dashboard from '../components/reutilizaveis/Dashboard'
import Usuarios from '../components/reutilizaveis/Usuarios'
import vincularProfissional from '../components/reutilizaveis/vincularProfissional'
import agendarVacina from '../components/reutilizaveis/agendarVacina'
import desvincularProfissional from '../components/reutilizaveis/desvincularProfissional'
import relatorios from '../components/reutilizaveis/relatorios'
Vue.use(Router)
const routes = [
    { path: '/paginaInicial', redirect: '/' },
    { path: '/', name:'paginaInicial', component: paginaInicial },
    {
        path: '/login', name: 'login', component: login,
        meta: {
            title: 'Sejá Bem-vindo!'
        }
    },
    {
        path: '/cadastro', name: 'Cadastro', component: Cadastro,
        meta: {
            title: "Cadastre-se aqui!"
        }
    },
    {
        path: '/logout', name: 'logout'
    },
    {
        path: '/auth/', component: () => import('../components/reutilizaveis/EstruturaPagina.vue'),
        children:[

            {
                path:'Dashboard', name: 'dashboard', component:Dashboard,
                meta: { title:'Página Inicial' }
            },

            {
                path:'usuarios', name: 'usuarios', component: Usuarios,
                meta: { title:'Gerenciar de Usuario' }
            },

            {
                path:'vinculoprofissionais', name: 'vinculoprofissionais', component: vincularProfissional,
                meta: { title:'Vincular Profissional' }
            },
            {
                path:'desvincularProfissional', name: 'desvincularProfissional', component: desvincularProfissional,
                meta: { title:'Vincular Profissional' }
            },
            {
                path: 'agendarVacina', name: 'agendarVacina',component: agendarVacina,
                meta: { title:'Agendar uma vacina' }
            },
            {
                path: 'relatorios', name: 'relatorios',component: relatorios,
                meta: { title:'Agendar uma vacina' }
            }

            
        ]
    },



];
const router = new Router({ routes, mode: 'history' })
export default router;