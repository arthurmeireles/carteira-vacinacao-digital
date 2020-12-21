import {API} from './config'

export default {
    getVacinas: () => {
        return API.get('/vacina')
    },
    adicionarVacina: (vacina) =>{
      return API.post('/vacina', vacina)
    },
    deletarVacina: (vacinaId) =>{
      return API.delete(`/vacina/${vacinaId}`)
    },
    getAplicacoes: () => {
      return API.get('/aplicacao')
    },
    getAplicacoesUsuario: (pacienteId) => {
      return API.get(`/aplicacao/${pacienteId}`)
    },
    buscarVacina: (query) => {
        return API.get(`/vacinaBusca?${query}`)
    },
    getVacinaEstabelecimento: (vacina_id) =>{
        return API.get(`/vacinaestabelecimento/${vacina_id}`)
    }
}
