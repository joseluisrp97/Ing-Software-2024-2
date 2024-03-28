import React, { useState } from 'react';
import './CRURentas.css';

function CRURentas() {
  const [rentas, setRentas] = useState([
    { idRenta: 1, idUsuario: '1', idPelicula: '1', fecha_renta: '2024-03-27', dias_de_renta: 5, estatus: 'Pendiente' }
  ]);

  const [nuevaRenta, setNuevaRenta] = useState({ idUsuario: '', idPelicula: '', fecha_renta: '', dias_de_renta: '', estatus: 'Pendiente' });
  const [editandoId, setEditandoId] = useState(null);
  const [edicion, setEdicion] = useState(null);

  const agregarRenta = () => {
    setRentas([...rentas, { ...nuevaRenta, idRenta: Date.now() }]);
    setNuevaRenta({ idUsuario: '', idPelicula: '', fecha_renta: '', dias_de_renta: '', estatus: 'Pendiente' }); 
  };

  const iniciarEdicion = (renta) => {
    setEditandoId(renta.idRenta);
    setEdicion({ ...renta });
  };

  const handleEditChange = (e) => {
    setEdicion({ ...edicion, [e.target.name]: e.target.value });
  };

  const guardarEdicion = () => {
    const nuevasRentas = rentas.map((renta) => {
      if (renta.idRenta === editandoId) {
        return { ...edicion };
      }
      return renta;
    });
    setRentas(nuevasRentas);
    setEditandoId(null);
  };

  const cancelarEdicion = () => {
    setEditandoId(null);
    setEdicion(null);
  };

  const eliminarRenta = (idRenta) => {
    const rentasActualizadas = rentas.filter(renta => renta.idRenta !== idRenta);
    setRentas(rentasActualizadas);
  };

  const handleInputChange = (e) => {
    setNuevaRenta({ ...nuevaRenta, [e.target.name]: e.target.value });
  };

  return (
    <div className="crud-rentas">
      <div className="agregar-renta">
        <input type="text" name="idUsuario" placeholder="ID Usuario" value={nuevaRenta.idUsuario} onChange={handleInputChange} />
        <input type="text" name="idPelicula" placeholder="ID Película" value={nuevaRenta.idPelicula} onChange={handleInputChange} />
        <input type="date" name="fecha_renta" placeholder="Fecha de Renta" value={nuevaRenta.fecha_renta} onChange={handleInputChange} />
        <input type="number" name="dias_de_renta" placeholder="Días de Renta" value={nuevaRenta.dias_de_renta} onChange={handleInputChange} />
        <select name="estatus" value={nuevaRenta.estatus} onChange={handleInputChange}>
          <option value="Pendiente">Pendiente</option>
          <option value="Entregado">Entregado</option>
        </select>
        <button onClick={agregarRenta}>Agregar Renta</button>
      </div>
      
      <div className="lista-rentas">
        {rentas.map((renta) => (
          <div key={renta.idRenta} className="renta">
            {editandoId === renta.idRenta ? (
              <div>
                <input type="text" name="idUsuario" value={edicion.idUsuario} onChange={handleEditChange} />
                <input type="text" name="idPelicula" value={edicion.idPelicula} onChange={handleEditChange} />
                <input type="date" name="fecha_renta" value={edicion.fecha_renta} onChange={handleEditChange} />
                <input type="number" name="dias_de_renta" value={edicion.dias_de_renta} onChange={handleEditChange} />
                <select name="estatus" value={edicion.estatus} onChange={handleEditChange}>
<option value="Pendiente">Pendiente</option>
<option value="Entregado">Entregado</option>
</select>
<button onClick={guardarEdicion}>Guardar</button>
<button onClick={cancelarEdicion}>Cancelar</button>
</div>
) : (
<div>
<div>ID Usuario: {renta.idUsuario}</div>
<div>ID Película: {renta.idPelicula}</div>
<div>Fecha de Renta: {renta.fecha_renta}</div>
<div>Días de Renta: {renta.dias_de_renta}</div>
<div>Estatus: {renta.estatus}</div>
<button onClick={() => iniciarEdicion(renta)}>Editar</button>
<button onClick={() => eliminarRenta(renta.idRenta)}>Eliminar</button>
</div>
)}
</div>
))}
</div>
</div>
);
}

export default CRURentas;
