import React, {useEffect, useState} from 'react';

export default function AdminPanel(){
  const [clientes, setClientes] = useState([]);
  useEffect(()=> {
    fetch('/api/clientes/').then(r=>r.json()).then(setClientes);
  },[]);
  return (
    <div className="mt-6">
      <h2 className="text-xl font-semibold mb-2">Panel Admin (simulado)</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {clientes.map(c=>(
          <div key={c.id_cliente} className="bg-white p-4 rounded shadow">
            <h3 className="font-bold">{c.nombre} {c.apellido}</h3>
            <p>{c.correo}</p>
          </div>
        ))}
      </div>
    </div>
  )
}