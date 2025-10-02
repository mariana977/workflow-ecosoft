import React, {useState} from 'react';
import { useNavigate } from 'react-router-dom';

export default function Register(){
  const [form, setForm] = useState({nombre:'', apellido:'', correo:'', contraseña_c:'', telefono:'', direccion:''});
  const nav = useNavigate();

  async function submit(e){
    e.preventDefault();
    const res = await fetch('/api/clientes/', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify(form)
    });
    if(res.ok) nav('/login');
    else alert('Error al registrar');
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <form onSubmit={submit} className="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h2 className="text-2xl font-semibold mb-4">Crear cuenta</h2>
        <input required placeholder="Nombre" className="w-full mb-2 p-2 border rounded" value={form.nombre} onChange={e=>setForm({...form,nombre:e.target.value})} />
        <input required placeholder="Apellido" className="w-full mb-2 p-2 border rounded" value={form.apellido} onChange={e=>setForm({...form,apellido:e.target.value})} />
        <input required type="email" placeholder="Correo" className="w-full mb-2 p-2 border rounded" value={form.correo} onChange={e=>setForm({...form,correo:e.target.value})} />
        <input required type="password" placeholder="Contraseña" className="w-full mb-2 p-2 border rounded" value={form.contraseña_c} onChange={e=>setForm({...form,contraseña_c:e.target.value})} />
        <input placeholder="Teléfono" className="w-full mb-2 p-2 border rounded" value={form.telefono} onChange={e=>setForm({...form,telefono:e.target.value})} />
        <input placeholder="Dirección" className="w-full mb-4 p-2 border rounded" value={form.direccion} onChange={e=>setForm({...form,direccion:e.target.value})} />
        <button className="w-full bg-green-600 text-white p-2 rounded">Registrarse</button>
      </form>
    </div>
  )
}