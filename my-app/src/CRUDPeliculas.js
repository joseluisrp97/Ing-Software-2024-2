import React, { useState } from 'react';
import './CRUDPeliculas.css'; // Asegúrate de tener este archivo CSS para estilos básicos

function CRUDPeliculas() {
  const [peliculas, setPeliculas] = useState([
    { idPelicula: 1, nombre: 'El Señor de los Anillos', genero: 'Fantasía', duracion: '178', inventario: 5 }
  ]);
  
  const [nuevaPelicula, setNuevaPelicula] = useState({ nombre: '', genero: '', duracion: '', inventario: '' });
  const [editandoId, setEditandoId] = useState(null);
  const [peliculaEnEdicion, setPeliculaEnEdicion] = useState(null);

  const agregarPelicula = () => {
    setPeliculas([...peliculas, { ...nuevaPelicula, idPelicula: Date.now(), duracion: parseInt(nuevaPelicula.duracion) }]);
    setNuevaPelicula({ nombre: '', genero: '', duracion: '', inventario: '' });
  };

  const iniciarEdicion = (pelicula) => {
    setEditandoId(pelicula.idPelicula);
    setPeliculaEnEdicion({ ...pelicula });
  };

  const handleEditChange = (e) => {
    const { name, value } = e.target;
    setPeliculaEnEdicion({ ...peliculaEnEdicion, [name]: name === "duracion" || name === "inventario" ? parseInt(value) : value });
  };

  const guardarEdicion = () => {
    const peliculasActualizadas = peliculas.map(pelicula => {
      if (pelicula.idPelicula === editandoId) {
        return { ...peliculaEnEdicion, duracion: parseInt(peliculaEnEdicion.duracion), inventario: parseInt(peliculaEnEdicion.inventario) };
      }
      return pelicula;
    });
    setPeliculas(peliculasActualizadas);
    setEditandoId(null);
  };

  const eliminarPelicula = (idPelicula) => {
    const peliculasActualizadas = peliculas.filter(pelicula => pelicula.idPelicula !== idPelicula);
    setPeliculas(peliculasActualizadas);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNuevaPelicula({ ...nuevaPelicula, [name]: name === "duracion" || name === "inventario" ? parseInt(value) : value });
  };

  return (
    <div className="crud-peliculas">
      <div className="agregar-pelicula">
        <input type="text" name="nombre" placeholder="Nombre" value={nuevaPelicula.nombre} onChange={handleInputChange} />
        <input type="text" name="genero" placeholder="Género" value={nuevaPelicula.genero} onChange={handleInputChange} />
        <input type="number" name="duracion" placeholder="Duración (min)" value={nuevaPelicula.duracion} onChange={handleInputChange} min="1" />
        <input type="number" name="inventario" placeholder="Inventario" value={nuevaPelicula.inventario} onChange={handleInputChange} min="0" />
        <button onClick={agregarPelicula}>Agregar Película</button>
      </div>
      
      <div className="lista-peliculas">
        {peliculas.map(pelicula => (
          <div key={pelicula.idPelicula} className="pelicula">
            {editandoId === pelicula.idPelicula ? (
              <div>
                <input type="text" name="nombre" value={peliculaEnEdicion.nombre} onChange={handleEditChange} />
                <input type="text" name="genero" value={peliculaEnEdicion.genero} onChange={handleEditChange} />
                <input type="number" name="duracion" value={peliculaEnEdicion.duracion} onChange={handleEditChange} min="1" />
                <input type="number" name="inventario" value={peliculaEnEdicion.inventario} onChange={handleEditChange} min="0" />
<button onClick={guardarEdicion}>Guardar</button>
<button onClick={() => setEditandoId(null)}>Cancelar</button>
</div>
) : (
<div>
<div>Nombre: {pelicula.nombre}</div>
<div>Género: {pelicula.genero}</div>
<div>Duración: {pelicula.duracion} min</div>
<div>Inventario: {pelicula.inventario}</div>
<button onClick={() => iniciarEdicion(pelicula)}>Editar</button>
<button onClick={() => eliminarPelicula(pelicula.idPelicula)}>Eliminar</button>
</div>
)}
</div>
))}
</div>
</div>
);
}

export default CRUDPeliculas;
