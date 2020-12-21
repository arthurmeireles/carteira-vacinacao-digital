import {API} from './config'

export default {
  getUsuarioLogado: () => {
      return API.get(`/usuarioLogado`,
      {
          headers: {
              'Authorization': 'Token '+localStorage.getItem('token')
          }
      })
  },

  updateUsuario: (usuarioId, usuario)=>{
      return API.put(`/conta/usuario/${usuarioId}`, usuario)
  }
}
