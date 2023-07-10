import http from '../http-common';

class LocationDataService {
    getAll(){
        return http.get("/location/")
    }

    get(id) {
        return http.get(`/location/${id}`)
    }

    create(data) {
        return http.post("/location/create/", data)
    }

    update(id, data){
        return http.put(`/location/${id}/`, data)
    }

    delete(id) {
        return http.delete(`/location/${id}`)
    }
}

export default new LocationDataService();