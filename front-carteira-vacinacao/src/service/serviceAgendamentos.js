import {API} from './config'

export default {
    adicionarAgendamento: (agendamento) => {
        return API.post('/agendamento', agendamento)
    },
    cancelarAgendamento:(usuarioId, agendamentoId )=>{
        return API.delete(`associar-paciente/${usuarioId}/${agendamentoId}`)
    },
    deletarAgendamento: (agendamentoId) => {
        return API.delete(`/agendamento/${agendamentoId}`)
    },
    getAgendamentos: () => {
        return API.get('/agendamento')
    },
    getAgendamentosMarcados: () => {
        return API.get('/agendamentoMarcados')
    },
    getAgendamentosDisponiveis: () => {
        return API.get('/agendamentoDisponivel')
    },
    getAgendamentosPaciente: (usuarioId) => {
        return API.get(`/agendamentoPaciente/${usuarioId}`)
    },



    baixarRelatorio: () => {
        window.location.href='http://localhost:8000/api/relatorio'
    }
}
