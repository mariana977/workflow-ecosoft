import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import IndexPage from './pages/Index';
import Register from './pages/Register';
import Login from './pages/Login';
import Home from './pages/Home';
import Header from './components/Header';

export default function App(){
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<IndexPage />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/home" element={<Home />} />
      </Routes>
    </BrowserRouter>
  )
}