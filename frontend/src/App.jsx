/* eslint-disable no-unused-vars */
import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import IndexPage from './pages/Index';
import Register from './pages/Register';
import Login from './pages/Login';
import Home from './pages/Home';
import Header from './components/Header';

export default function App() {
  return (
    <div className="bg-green-500 text-white text-xl font-bold p-4 rounded-b-lg shadow-md">
      ¡Tailwind está funcionando!
    </div>
  )
}
