import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react';
import ClientList from "./components/Clients/ClientList"

function App() {
  return (
    <div className="container">
      <BrowserRouter>
        <Routes>
          <Route path="clients/" element={<ClientList />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
