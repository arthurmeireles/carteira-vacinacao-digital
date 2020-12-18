import Vue from 'vue';
import Router from 'vue-router';
import login from '../components/paginasGerais/login';
import Cadastro  from '../components/paginasGerais/cadastro';
import paginaInicial from '../components/paginasGerais/paginaInicial'



Vue.use(Router)
const routes = [
    { path: '/paginaInicial', name:'paginaInicial', redirect: '/' },
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
            // Recarrega a Página inicial colocando o component dashboard
            // {
            //     path: '/', redirect:'/Dashboard'
            // },
            // {
            //     path:'Dashboard', name: 'paginaInicial', component:Dashboard,
            //     meta: { title:'Página Inicial' }
            // },
            // {
            //     path: 'explorar', name: 'explorar', component: listarPublicacoes,
            //     meta: {title: 'Explorar'}
            // },
        ]
    },



];
const router = new Router({ routes, mode: 'history' })
export default router;