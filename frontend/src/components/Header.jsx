import React from 'react';
import { Link } from 'react-router-dom';
export default function Header(){
  return (
    <header className="bg-white shadow">
      <div className="max-w-6xl mx-auto p-4 flex justify-between items-center">
        <Link to="/" className="text-xl font-bold text-green-700">Ecosoft</Link>
        <nav className="flex gap-4">
          <Link to="/register" className="text-green-600">Registro</Link>
          <Link to="/login" className="text-green-600">Login</Link>
          <Link to="/home" className="text-green-600">Home</Link>
        </nav>
      </div>
    </header>
  )
}