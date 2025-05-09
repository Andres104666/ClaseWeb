import { Investigadores_lista } from '../components/investigadores_lista.jsx';

export function Investigadores() {
    return (
        <div className="min-h-screen bg-gray-50 p-6">
            <h1 className="text-3xl font-bold text-center mb-8">
                Página de Investigadores
            </h1>
            <Investigadores_lista />
        </div>
    );
}

