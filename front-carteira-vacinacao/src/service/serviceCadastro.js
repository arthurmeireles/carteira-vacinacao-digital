import {API} from './config'

export default {
  cadastrarUsuario: (usuario) => {
      return API.post('/registro', usuario)
  }

}
