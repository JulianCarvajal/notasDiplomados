//Ontenemos los valores de los campos de contraseñas
Password = document.getElementById('Password');
Password2 = document.getElementById('Password2');


const verificarPasswords = () => {

    // Verificamos si las constraseñas no coinciden
    if (Password.value != Password2.value) {
    
        // Si las constraseñas no coinciden mostramos un mensaje
        document.getElementById("error").classList.add("mostrar");
    
        return false;
    }
    
    else {
    
        // Si las contraseñas coinciden ocultamos el mensaje de error
        document.getElementById("error").classList.remove("mostrar");
    
        // Mostramos un mensaje mencionando que las Contraseñas coinciden
        document.getElementById("ok").classList.remove("ocultar");
    
        // Desabilitamos el botón de login
        document.getElementById("login").disabled = true;
    
        // Refrescamos la página (Simulación de envío del formulario)
        setTimeout(function() {
        location.reload();
        }, 3000);
    
        return true;
    }
}

verificarPasswords()