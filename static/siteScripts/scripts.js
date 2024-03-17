// Función para manejar el clic en los botones
function handleClick(event) {    
    const botonPresionado = event.target;                               // obtiene el elemento que desencadenó el evento    
    var myId = botonPresionado.value                                    // obtiene su valor 'value'
    document.getElementById("formId").setAttribute("value", myId);      //actualiza el valor 'value' del form    
}

// Obtener todos los botones y asignar la función al evento clic
const botones = document.querySelectorAll('.boton');
botones.forEach(boton => {
    boton.addEventListener('click', handleClick);
});