import { useForm } from "react-hook-form";
import { useNavigate, useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';
import { CreateInvestigador, DeleteInvestigador, UpdateInvestigador } from '../api/investigadores.api.jsx';

export function InvestigadoresFormPage() {
    const { register, handleSubmit, formState: { errors }, setValue } = useForm();
    const [usuarios, setUsuarios] = useState([]);
    const [areas, setAreas] = useState([]);
    const [niveledu, setNivelEdu] = useState([]);
    const [nivelsnii, setNivelSnii] = useState([]);
    const navigate = useNavigate();
    const params = useParams();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function fetchUsuarios() {
            try {
                const response = await axios.get('http://localhost:8000/api/Usuario/');
                setUsuarios(response.data);
            } catch (error) {
                console.error('Error al cargar los usuarios:', error);
            }
        }

        async function fetchAreas() {
            try {
                const response = await axios.get('http://localhost:8000/api/Areas/');
                setAreas(response.data);
            } catch (error) {
                console.error('Error al cargar las áreas:', error);
            }
        }

        async function fetchNivelEdu() {
            try {
                const response = await axios.get('http://localhost:8000/api/NivelEdu/');
                setNivelEdu(response.data);
            } catch (error) {
                console.error('Error al cargar los niveles educativos:', error);
            }
        }

        async function fetchNivelSnii() {
            try {
                const response = await axios.get('http://localhost:8000/api/NivelSNII/');
                setNivelSnii(response.data);
            } catch (error) {
                console.error('Error al cargar los niveles SNII:', error);
            }
        }

        async function fetchInvestigador() {
            if (params.id) {
                try {
                    const response = await axios.get(`http://localhost:8000/api/Investigadores/${params.id}/`);
                    const investigador = response.data;
                    
                    // Establecer los valores del formulario
                    setValue("nombre", investigador.nombre);
                    setValue("tel", investigador.tel);
                    setValue("email", investigador.email);
                    setValue("area", investigador.area);
                    setValue("usuario", investigador.usuario);
                    setValue("nivel_edu", investigador.nivel_edu);
                    setValue("snii", investigador.snii);
                    setValue("esatus", investigador.esatus.toString());
                } catch (error) {
                    console.error('Error al cargar el investigador:', error);
                }
            }
            setLoading(false);
        }

        fetchUsuarios();
        fetchAreas();
        fetchNivelEdu();
        fetchNivelSnii();
        fetchInvestigador();

    }, [params.id, setValue]);

    const onSubmit = handleSubmit(async (data) => {
        try {
            if (params.id) {
                // Editar investigador existente
                const response = await UpdateInvestigador(params.id, data);
                console.log('Investigador actualizado:', response.data);
                alert('Investigador actualizado exitosamente');
            } else {
                // Crear un nuevo investigador
                const response = await CreateInvestigador(data);
                console.log('Investigador creado:', response.data);
                alert('Investigador creado exitosamente');
            }
            navigate("/investigadores");
        } catch (error) {
            console.error('Error al guardar el investigador:', error);
            alert('Hubo un error al guardar el investigador');
        }
    });

    if (loading) {
        return (
            <div className="flex justify-center items-center h-screen">
                <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-50 p-6">
            <h1 className="text-2xl font-semibold text-gray-800 mb-6">
                {params.id ? 'Editar Investigador' : 'Crear Nuevo Investigador'}
            </h1>
            
            <form onSubmit={onSubmit} className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {/* Información personal */}
                    <div className="space-y-4">
                        <div>
                            <label htmlFor="nombre" className="block text-sm font-medium text-gray-700 mb-1">
                                Nombre
                            </label>
                            <input 
                                type="text" 
                                id="nombre"
                                placeholder="Nombre completo" 
                                className={`w-full px-3 py-2 border ${errors.nombre ? 'border-red-500' : 'border-gray-300'} rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500`}
                                {...register("nombre", { required: true })} 
                            />
                            {errors.nombre && <p className="mt-1 text-sm text-red-500">Este campo es requerido</p>}
                        </div>

                        <div>
                            <label htmlFor="tel" className="block text-sm font-medium text-gray-700 mb-1">
                                Teléfono
                            </label>
                            <input 
                                type="text" 
                                id="tel"
                                placeholder="Teléfono de contacto" 
                                className={`w-full px-3 py-2 border ${errors.tel ? 'border-red-500' : 'border-gray-300'} rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500`} 
                                {...register("tel", { required: true })} 
                            />
                            {errors.tel && <p className="mt-1 text-sm text-red-500">Este campo es requerido</p>}
                        </div>

                        <div>
                            <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
                                Email
                            </label>
                            <input 
                                type="email" 
                                id="email"
                                placeholder="Correo electrónico" 
                                className={`w-full px-3 py-2 border ${errors.email ? 'border-red-500' : 'border-gray-300'} rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500`}
                                {...register("email", { required: true })} 
                            />
                            {errors.email && <p className="mt-1 text-sm text-red-500">Este campo es requerido</p>}
                        </div>

                        <div>
                            <label htmlFor="usuario" className="block text-sm font-medium text-gray-700 mb-1">
                                Usuario
                            </label>
                            <select 
                                id="usuario"
                                className={`w-full px-3 py-2 border ${errors.usuario ? 'border-red-500' : 'border-gray-300'} rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white`}
                                {...register("usuario", { required: true })}
                            >
                                <option value="">Seleccione un usuario</option>
                                {usuarios.map(usuario => (
                                    <option key={usuario.id} value={usuario.id}>
                                        {usuario.nombre} ({usuario.email})
                                    </option>
                                ))}
                            </select>
                            {errors.usuario && <p className="mt-1 text-sm text-red-500">Este campo es requerido</p>}
                        </div>
                    </div>

                    {/* Información académica */}
                    <div className="space-y-4">
                        <div>
                            <label htmlFor="area" className="block text-sm font-medium text-gray-700 mb-1">
                                Área
                            </label>
                            <select 
                                id="area"
                                className={`w-full px-3 py-2 border ${errors.area ? 'border-red-500' : 'border-gray-300'} rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white`}
                                {...register("area", { required: true })}
                            >
                                <option value="">Seleccione un área</option>
                                {areas.map(area => (
                                    <option key={area.id} value={area.id}>
                                        {area.nombre}
                                    </option>
                                ))}
                            </select>
                            {errors.area && <p className="mt-1 text-sm text-red-500">Este campo es requerido</p>}
                        </div>

                        <div>
                            <label htmlFor="nivel_edu" className="block text-sm font-medium text-gray-700 mb-1">
                                Nivel Educativo
                            </label>
                            <select 
                                id="nivel_edu"
                                className={`w-full px-3 py-2 border ${errors.nivel_edu ? 'border-red-500' : 'border-gray-300'} rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white`}
                                {...register("nivel_edu", { required: true })}
                            >
                                <option value="">Seleccione Nivel Educativo</option>
                                {niveledu.map(nivel => (
                                    <option key={nivel.id} value={nivel.id}>
                                        {nivel.descripcion}
                                    </option>
                                ))}
                            </select>
                            {errors.nivel_edu && <p className="mt-1 text-sm text-red-500">Este campo es requerido</p>}
                        </div>

                        <div>
                            <label htmlFor="snii" className="block text-sm font-medium text-gray-700 mb-1">
                                Nivel SNII
                            </label>
                            <select 
                                id="snii"
                                className={`w-full px-3 py-2 border ${errors.snii ? 'border-red-500' : 'border-gray-300'} rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white`}
                                {...register("snii", { required: true })}
                            >
                                <option value="">Seleccione Nivel SNII</option>
                                {nivelsnii.map(nivel => (
                                    <option key={nivel.id} value={nivel.id}>
                                        {nivel.descripcion}
                                    </option>
                                ))}
                            </select>
                            {errors.snii && <p className="mt-1 text-sm text-red-500">Este campo es requerido</p>}
                        </div>

                        <div>
                            <label htmlFor="esatus" className="block text-sm font-medium text-gray-700 mb-1">
                                Estado
                            </label>
                            <select 
                                id="esatus"
                                className={`w-full px-3 py-2 border ${errors.esatus ? 'border-red-500' : 'border-gray-300'} rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white`}
                                {...register("esatus", { required: true })}
                            >
                                <option value="">Seleccione el estado</option>
                                <option value="true">Activo</option>
                                <option value="false">Inactivo</option>
                            </select>
                            {errors.esatus && <p className="mt-1 text-sm text-red-500">Este campo es requerido</p>}
                        </div>
                    </div>
                </div>

                {/* Botones */}
                <div className="flex space-x-4 pt-4 border-t border-gray-200">
                    <button 
                        type="submit" 
                        className="px-6 py-2 bg-blue-600 text-black font-medium rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
                    >
                        {params.id ? 'Actualizar' : 'Guardar'}
                    </button>

                    <button 
                        type="button"
                        onClick={() => navigate("/investigadores")}
                        className="px-6 py-2 bg-blue-600 text-black font-medium rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
                    >
                        Cancelar
                    </button>

                    {params.id && (
                        <button 
                            type="button"
                            onClick={async () => {
                                const accept = window.confirm('¿Está seguro de eliminar este investigador?');
                                if (accept) {
                                    try {
                                        await DeleteInvestigador(params.id);
                                        navigate("/investigadores");
                                    } catch (error) {
                                        console.error('Error al eliminar el investigador:', error);
                                    }
                                }
                            }}
                            className="px-6 py-2 bg-red-600 text-white font-medium rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 transition-colors ml-auto"
                        >
                            Eliminar
                        </button>
                    )}
                </div>
            </form>
        </div>
    );
}