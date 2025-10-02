import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';

export default function Login(){
  const [form, setForm] = useState({correo:'', contraseña_c:''});
  const nav = useNavigate();

  async function submit(e){
    e.preventDefault();
    // naive auth: try to find cliente with email (the backend doesn't implement auth token here)
    const res = await fetch(`/api/clientes/`);
    const data = await res.json();
    const user = data.find(u=>u.correo === form.correo);
    if(user) {
      // store in localStorage and go home
      localStorage.setItem('ecosoft_user', JSON.stringify(user));
      nav('/home');
    } else {
      alert('Usuario no encontrado');
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <form onSubmit={submit} className="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h2 className="text-2xl font-semibold mb-4">Iniciar sesión</h2>
        <input required type="email" placeholder="Correo" className="w-full mb-2 p-2 border rounded" value={form.correo} onChange={e=>setForm({...form,correo:e.target.value})} />
        <input required type="password" placeholder="Contraseña" className="w-full mb-4 p-2 border rounded" value={form.contraseña_c} onChange={e=>setForm({...form,contraseña_c:e.target.value})} />
        <button className="w-full bg-green-600 text-white p-2 rounded">Entrar</button>
      </form>
    </div>
  )
}