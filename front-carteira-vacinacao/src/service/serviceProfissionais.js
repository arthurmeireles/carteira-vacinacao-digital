import {API} from './config'

export default {
    getProfissionais: () => {
        return API.get('/profissional')
    },

    getProfissional: (usuarioId) => {
        return API.get(`/profissional/${usuarioId}`)
    },

    getProfissionalPorCPF: (cpf) => {
        return API.get(`/buscarProfissionalPorCPF/${cpf}`)
    },

    getEstabelecimentoPorCNES: (cnes) => {
        return API.get(`/buscarEstabelecimentoPorCNES/${cnes}`)
    },

    buscarProfissional:(query)=>{
        return API.get(`/usuario?${query}`)
    },

    buscarEstabelecimento: (query) => {
        return API.get(`/buscarEstabelecimento?${query}`)
    },

    vincularProfissional: (usuario_id, estabelecimento_id) => {
        return API.post(`/associar-profissional/${usuario_id}/${estabelecimento_id}`)
    },
    desvincularProfissional: (usuario_id, estabelecimento_id) => {
        return API.delete(`/associar-profissional/${usuario_id}/${estabelecimento_id}`)
    }

}
