import axios from 'axios';

var Api =  {
    getTemperature: function(){
        return axios.get("/api/temperature")
    },

    test: function(){
        return axios.get("/api/test")
    }
}

export default Api;