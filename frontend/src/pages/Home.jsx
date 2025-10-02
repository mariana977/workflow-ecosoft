import React, {useEffect, useState} from 'react';
import AdminPanel from '../components/AdminPanel';

export default function Home(){
  const [user, setUser] = useState(null);
  useEffect(()=> {
    const u = localStorage.getItem('ecosoft_user');
    if(u) setUser(JSON.parse(u));
  },[]);
  return (
    <div className="min-h-screen p-8 bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Panel principal</h1>
      {user ? (
        <div>
          <p>Bienvenido {user.nombre} {user.apellido}</p>
          <AdminPanel />
        </div>
      ) : (
        <p>Debes iniciar sesión</p>
      )}
    </div>
  )
}