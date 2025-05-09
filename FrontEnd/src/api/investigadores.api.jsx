import axios from "axios";

const api = axios.create({
    baseURL: 'http://localhost:8000/api/Investigador/'
});

export const Getallinvestigadores = () => {
    return api.get('/'); 
};

export const GetInvestigadorById = (id) => {
    return api.get(`/${id}/`); // Backend
};

export const UpdateInvestigador = (id, data) => {
    return api.put(`/${id}/`, data); 
};

export const CreateInvestigador = (Investigador) => {
    return api.post('/', Investigador); 
};

export const DeleteInvestigador = (id) => {
    return api.delete(`/${id}/`); 
};