
import { Link } from 'react-router-dom';

export function Navigation() {
    return (
        <nav className="bg-blue-950 text-white h-screen w-50 fixed top-0 left-0 shadow-md">
            <div className="p-1">
                <h1 className="text- font-bold mb-3">CITAEQ</h1>
                <ul className="space-y-4">
                    <li>
                        <Link
                            to="/home"
                            className="block text-blue-500 hover:bg-lightblue-700 p-2 rounded"
                        >
                            Home
                        </Link>
                    </li>
                    <li>
                        <Link
                            to="/investigadores"
                            className="block text-white hover:bg-blue-700 p-2 rounded"
                        >
                            Investigadores
                        </Link>
                    </li>
                </ul>
            </div>
        </nav>
    );
}