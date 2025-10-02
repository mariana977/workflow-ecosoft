import React from 'react';
import { Link } from 'react-router-dom';

export default function IndexPage() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-green-50 to-white">
      <header className="text-center py-10">
        <h1 className="text-5xl font-extrabold text-green-700">¡Bienvenidos a EcoSoft! ♻️</h1>
        <p className="text-gray-600 mt-3 max-w-2xl mx-auto"> 
          Reducimos residuos, optimizamos recursos y cuidamos el medio ambiente. 

        </p>
        <div className="mt-6 flex justify-center gap-4">
          <Link to="/register" className="px-6 py-2 bg-green-600 text-white rounded-lg shadow hover:bg-green-700">
            Registrarse
          </Link>
          <Link to="/login" className="px-6 py-2 border border-green-600 text-green-600 rounded-lg hover:bg-green-50">
            Iniciar sesión
          </Link>
        </div>
      </header>

      {/* Nosotros */}
      <section className="py-12 px-6 bg-green-100 text-center">
  <h2 className="text-2xl font-bold text-green-800 mb-4">Nosotros</h2>
  <p className="text-gray-700 max-w-3xl mx-auto">
    Somos una empresa enfocada en optimizar la recolección, el uso de recursos 
    y el control de insumos generando beneficios para empresas y el medio ambiente.
  </p>
</section>


      {/* Productos */}
      <section className="py-12 px-6">
        <h2 className="text-2xl font-bold text-green-800 text-center mb-8">Productos</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="bg-white shadow rounded-xl p-4 text-center">
            <h3 className="font-bold text-green-700">Plástico</h3>
            <p className="text-gray-600 text-sm">Botellas de agua y refrescos, envases de champú y productos de limpieza.</p>
          </div>
          <div className="bg-white shadow rounded-xl p-4 text-center">
            <h3 className="font-bold text-green-700">Papel</h3>
            <p className="text-gray-600 text-sm">Periódicos, revistas, folletos, sobres y hojas de papel.</p>
          </div>
          <div className="bg-white shadow rounded-xl p-4 text-center">
            <h3 className="font-bold text-green-700">Cartón</h3>
            <p className="text-gray-600 text-sm">Cajas de cartón, cartón corrugado y plano.</p>
          </div>
          <div className="bg-white shadow rounded-xl p-4 text-center">
            <h3 className="font-bold text-green-700">Distribución</h3>
            <p className="text-gray-600 text-sm">Pacas de papel, cartón o plástico y pacas mixtas.</p>
          </div>
        </div>
      </section>

      {/* Beneficios */}
      <section className="py-12 px-6 bg-green-50">
        <h2 className="text-2xl font-bold text-green-800 text-center mb-6">Beneficios</h2>
        <ul className="max-w-3xl mx-auto list-disc list-inside text-gray-700 space-y-2">
          <li>Impacto ambiental positivo</li>
          <li>Plataforma digital fácil de usar</li>
          <li>Acceso a diferentes necesidades</li>
          <li>Ahorro en costos de recolección y transporte</li>
          <li>Datos seguros y gestión centralizada</li>
        </ul>
      </section>

      {/* Footer */}
      <footer className="text-center py-6 text-gray-500 text-sm">
        © {new Date().getFullYear()} EcoSoft - Todos los derechos reservados
      </footer>
    </div>
  );
}
