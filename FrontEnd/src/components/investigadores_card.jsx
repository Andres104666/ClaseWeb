import {useNavigate} from 'react-router-dom'


// export function InvestigadoresCard({Investigador}) {

//   const navigate = useNavigate()

//   return (
//     <div onClick={()=> {
//       navigate('/investigadores/' + Investigador.id)
//     }}>
//         <h1>{Investigador.nombre}</h1>
//         <p>{Investigador.area}</p>
//         <hr/>
//     </div>
//   );
// }

export function InvestigadoresCard({ Investigador }) {
  const navigate = useNavigate();

  return (
      <div
          onClick={() => {
              navigate('/investigadores/' + Investigador.id);
          }}
          className="bg-white shadow-md rounded-lg p-4 cursor-pointer hover:shadow-lg transition-shadow"
      >
          <h1 className="text-xl font-bold text-gray-800 mb-2">
              {Investigador.nombre}
          </h1>
          <p className="text-gray-600">{Investigador.area}</p>
          <hr className="mt-4 border-gray-300" />
      </div>
  );
}