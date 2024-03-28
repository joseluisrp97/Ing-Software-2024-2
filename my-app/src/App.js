import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import CRUDClientes from './CRUDClientes'; 
import CRUDPeliculas from './CRUDPeliculas'; 
import CRURentas from './CRURentas'; 
import './App.css'; 
function App() {
  return (
    <Router>
      <div className="App">
        <nav>
          <h1>Bienvenido a Cine Manager</h1>
          <div className="navigation-buttons">
            <Link to="/usuarios"><button>Usuarios</button></Link>
            <Link to="/peliculas"><button>Películas</button></Link>
            <Link to="/rentas"><button>Rentas</button></Link>
          </div>
        </nav>
        <Routes>
          <Route path="/" element={<WelcomeMessage />} />
          <Route path="/usuarios" element={<CRUDClientes />} />
          <Route path="/peliculas" element={<CRUDPeliculas />} />
          <Route path="/rentas" element={<CRURentas />} />
        </Routes>
      </div>
    </Router>
  );
}

function WelcomeMessage() {
  return (
    <div className="welcome-message">
      <p>Gestiona tus películas, usuarios y rentas con facilidad.</p>
    </div>
  );
}

export default App;
