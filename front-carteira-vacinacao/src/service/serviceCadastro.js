import {API} from './config'

export default {
  cadastrarUsuario: (usuario) => {
      return API.post('/registro', usuario)
  },

    criaCartaoVacinacao: (usuarioId) =>{
        console.log(usuarioId)
        return API.post('/carteira-vacinacao', usuarioId)
    }

}
