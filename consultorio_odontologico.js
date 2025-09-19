// consultorio_odontologico.js
// Gestión de turnos odontológicos en el navegador (localStorage)

class TurnoManager {
    constructor() {
        this.turnos = this.cargarTurnos();
    }

    cargarTurnos() {
        const data = localStorage.getItem('turnosConsultorio');
        return data ? JSON.parse(data) : [];
    }

    guardarTurnos() {
        localStorage.setItem('turnosConsultorio', JSON.stringify(this.turnos));
    }

    agregarTurno(turno) {
        this.turnos.push(turno);
        this.guardarTurnos();
    }

    cancelarTurno(codigo) {
        this.turnos = this.turnos.filter(t => t.codigo !== codigo);
        this.guardarTurnos();
    }

    modificarTurno(codigo, cambios) {
        const idx = this.turnos.findIndex(t => t.codigo === codigo);
        if (idx !== -1) {
            this.turnos[idx] = { ...this.turnos[idx], ...cambios };
            this.guardarTurnos();
        }
    }

    obtenerTurnos() {
        return this.turnos;
    }

    filtrarPorArancel(arancel) {
        return this.turnos.filter(t => t.arancel === arancel);
    }

    mayorArancel() {
        const max = Math.max(...this.turnos.map(t => t.arancel));
        return this.turnos.filter(t => t.arancel === max);
    }

    filtrarPorProfesional(nombre) {
        return this.turnos.filter(t => t.profesional === nombre);
    }
}

// Utilidades para la interfaz
function mostrarTurnos(turnos) {
    const lista = document.getElementById('lista-turnos');
    lista.innerHTML = '';
    if (turnos.length === 0) {
        lista.innerHTML = '<p>No hay turnos asignados.</p>';
        return;
    }
    turnos.forEach(t => {
        const div = document.createElement('div');
        div.className = 'turno';
        div.innerHTML = `<strong>Código:</strong> ${t.codigo} | <strong>Paciente:</strong> ${t.apellido} | <strong>DNI:</strong> ${t.dni} | <strong>Obra Social:</strong> ${t.obraSocial} | <strong>Arancel:</strong> $${t.arancel} | <strong>Fecha:</strong> ${t.fecha} | <strong>Hora:</strong> ${t.hora} | <strong>Motivo:</strong> ${t.motivo} | <strong>Profesional:</strong> ${t.profesional}
        <button onclick="cancelarTurno('${t.codigo}')">Cancelar</button>`;
        lista.appendChild(div);
    });
}

function limpiarFormulario() {
    document.getElementById('form-turno').reset();
}

// Inicialización y eventos
const manager = new TurnoManager();
document.addEventListener('DOMContentLoaded', function() {
    mostrarTurnos(manager.obtenerTurnos());

    document.getElementById('form-turno').addEventListener('submit', function(e) {
        e.preventDefault();
        const codigo = document.getElementById('codigo').value.trim();
        const apellido = document.getElementById('nombre').value.trim();
        const dni = document.getElementById('dni').value.trim();
        const obraSocial = document.getElementById('obraSocial').value;
        let arancel = 0;
        if (obraSocial === 'OSDE') arancel = 0;
        else if (obraSocial === 'SWISS') arancel = 1500;
        else if (obraSocial === 'PARTICULAR') arancel = 5000;
        const fecha = document.getElementById('fecha').value;
        const hora = document.getElementById('hora').value;
        const motivo = document.getElementById('motivo').value;
        const profesional = document.getElementById('profesional').value;

        // Validaciones básicas
        if (!codigo.match(/^\d+$/) || manager.turnos.some(t => t.codigo === codigo)) {
            alert('Código inválido o repetido.');
            return;
        }
        if (!apellido.match(/^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{3,}$/)) {
            alert('Apellido inválido.');
            return;
        }
        if (!dni.match(/^\d{7,8}$/)) {
            alert('DNI inválido.');
            return;
        }
        if (!fecha || !hora) {
            alert('Fecha y hora requeridas.');
            return;
        }
        // No permitir duplicados de fecha, hora y profesional
        if (manager.turnos.some(t => t.fecha === fecha && t.hora === hora && t.profesional === profesional)) {
            alert('Ya existe un turno asignado en esa fecha, hora y profesional.');
            return;
        }

        manager.agregarTurno({ codigo, apellido, dni, obraSocial, arancel, fecha, hora, motivo, profesional });
        mostrarTurnos(manager.obtenerTurnos());
        limpiarFormulario();
        document.getElementById('confirmacion').style.display = 'block';
        setTimeout(() => {
            document.getElementById('confirmacion').style.display = 'none';
        }, 2000);
    });
});

// Función global para cancelar turnos
function cancelarTurno(codigo) {
    manager.cancelarTurno(codigo);
    mostrarTurnos(manager.obtenerTurnos());
}

// Puedes agregar más funciones para modificar, filtrar, etc. según lo necesites
