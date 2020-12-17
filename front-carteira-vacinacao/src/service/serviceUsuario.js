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
  curtir: (idUsuario) => {
      return API.get(`/publicacao/curtir/${idUsuario}/`)
  },
  descurtir: (idPublicacao) => {
      return API.delete(`/publicacao/curtir/${idPublicacao}/`)
  },
  criarUsuario:(usuario)=>{
      return API.post('/conta/registrar',usuario)
  },
  buscar: (query) => {
      return API.get(`/usuarios?${query}`)
  },
  updateUsuario: (usuarioId, usuario)=>{
      return API.put(`/conta/usuario/${usuarioId}`,usuario)
  }
}
