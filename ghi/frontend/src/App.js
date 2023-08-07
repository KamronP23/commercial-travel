import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react';
import ClientList from "./components/Clients/ClientList"
import FrequentTravelGroupList from './components/FrequentTravelGroups/FrequentTravelGroupList';

function App() {
  return (
    <div className="container">
      <BrowserRouter>
        <Routes>
          <Route path="clients/" element={<ClientList />} />
          <Route path="groups/" element={<FrequentTravelGroupList />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
