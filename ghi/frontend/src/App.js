import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react';
import ClientList from "./components/Clients/ClientList"
import ClientDetail from "./components/Clients/ClientDetail"
import FrequentTravelGroupList from './components/FrequentTravelGroups/FrequentTravelGroupList';
import FrequentTravelGroupDetail from './components/FrequentTravelGroups/FrequentTravelGroupDetail';
import FlightList from './components/Flights/FlightList';
import HotelList from './components/Hotels/HotelList';
import PackageList from './components/Packages/PackageList';
import PackageDetail from './components/Packages/PackageDetail';
function App() {
  return (
    <div className="container">
      <BrowserRouter>
        <Routes>
          <Route path="clients/" element={<ClientList />} />
          <Route path="clients/:id" element={<ClientDetail />} />
          <Route path="groups/" element={<FrequentTravelGroupList />} />
          <Route path="groups/:id" element={<FrequentTravelGroupDetail />} />
          <Route path="flights/" element={<FlightList />} />
          <Route path="hotels/" element={<HotelList />} />
          <Route path="packages/" element={<PackageList />} />
          <Route path="packages/:id" element={<PackageDetail />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
