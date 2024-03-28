import React, { useState } from 'react';
import './CRUDClientes.css';

function CRUDClientes() {
  const [clientes, setClientes] = useState([
    { id: 1, nombre: 'Juan', apPat: 'Pérez', apMat: 'López', correo: 'juan.perez@example.com' }
  ]);
  
  const [nuevoCliente, setNuevoCliente] = useState({ nombre: '', apPat: '', apMat: '', correo: '' });
  const [editandoId, setEditandoId] = useState(null);
  const [clienteEnEdicion, setClienteEnEdicion] = useState({ nombre: '', apPat: '', apMat: '', correo: '' });

  const agregarCliente = () => {
    setClientes([...clientes, { ...nuevoCliente, id: Date.now() }]);
    setNuevoCliente({ nombre: '', apPat: '', apMat: '', correo: '' }); 
  };

  const iniciarEdicion = (cliente) => {
    setEditandoId(cliente.id);
    setClienteEnEdicion({ ...cliente });
  };

  const handleEditChange = (e) => {
    setClienteEnEdicion({ ...clienteEnEdicion, [e.target.name]: e.target.value });
  };

  const guardarEdicion = () => {
    const clientesActualizados = clientes.map(cliente => {
      if (cliente.id === editandoId) {
        return { ...clienteEnEdicion };
      }
      return cliente;
    });
    setClientes(clientesActualizados);
    cancelarEdicion();
  };

  const cancelarEdicion = () => {
    setEditandoId(null);
    setClienteEnEdicion({ nombre: '', apPat: '', apMat: '', correo: '' });
  };

  const eliminarCliente = (id) => {
    const clientesActualizados = clientes.filter(cliente => cliente.id !== id);
    setClientes(clientesActualizados);
  };

  const handleInputChange = (e) => {
    setNuevoCliente({ ...nuevoCliente, [e.target.name]: e.target.value });
  };

  return (
    <div className="crud-clientes">
      <div className="agregar-cliente">
        {/* Formulario para agregar nuevo cliente */}
        <input type="text" name="nombre" placeholder="Nombre" value={nuevoCliente.nombre} onChange={handleInputChange} />
        <input type="text" name="apPat" placeholder="Apellido Paterno" value={nuevoCliente.apPat} onChange={handleInputChange} />
        <input type="text" name="apMat" placeholder="Apellido Materno" value={nuevoCliente.apMat} onChange={handleInputChange} />
        <input type="email" name="correo" placeholder="Correo Electrónico" value={nuevoCliente.correo} onChange={handleInputChange} />
        <button onClick={agregarCliente}>Agregar Cliente</button>
      </div>
      
      <div className="lista-clientes">
        {clientes.map(cliente => (
          <div key={cliente.id} className="cliente">
            {editandoId === cliente.id ? (
              <div>
                {/* Formulario de edición */}
                <input type="text" name="nombre" value={clienteEnEdicion.nombre} onChange={handleEditChange} />
                <input type="text" name="apPat" value={clienteEnEdicion.apPat} onChange={handleEditChange} />
                <input type="text" name="apMat" value={clienteEnEdicion.apMat} onChange={handleEditChange} />
                <input type="email" name="correo" value={clienteEnEdicion.correo} onChange={handleEditChange} />
                <button onClick={guardarEdicion}>Guardar</button>
                <button onClick={cancelarEdicion}>Cancelar</button>
              </div>
            ) : (
              <div>
                <div>{cliente.nombre} {cliente.apPat} {cliente.apMat}</div>
                <div>{cliente.correo}</div>
                <button onClick={() => iniciarEdicion(cliente)}>Editar</button>
                <button onClick={() => eliminarCliente(cliente.id)}>Eliminar</button>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default CRUDClientes;
