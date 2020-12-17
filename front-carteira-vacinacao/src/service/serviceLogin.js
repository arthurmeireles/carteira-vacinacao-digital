import {API} from './config'


export default {
    login:(usuario)=>{
        return API.post('/login', usuario)
    },
}