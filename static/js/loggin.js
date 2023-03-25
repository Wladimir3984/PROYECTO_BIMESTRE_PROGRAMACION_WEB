//Se ejecuta el document.ready para que primero cargue el documento
// y una vez que cargue completamente, se ejecutara js
$(document).ready(function () {
    $("#mensaje").hide();
    //Funcion para validar el Loggin
    const validacion = () => {
        //Creamos las variables
        const usuario_in = $("#usuario").val();
        const contrasenia_in = $("#contrasenia").val();
        //Validacion
        if (usuario_in == "admin" && contrasenia_in == "admin") {
            //Mensaje correcto
            $("#mensaje").html("Inicio de session exitoso.");
            $("#mensaje").removeClass("incorrecto");
            $("#mensaje").addClass("correcto");
            $("#mensaje").show();
            return true
        } else {
            //Mensaje incorrecto
            $("#mensaje").html("Usuario y/o contraseña invalido<br>Intente nuevamente");
            $("#mensaje").removeClass("correcto");
            $("#mensaje").addClass("incorrecto");
            $("#mensaje").show();
            return false
        };
    };
    //Boton de ingresar
    $("#ingresar").click(function (e) {
        //Detenemos el evento `Submit` para que no envie los datos aun
        e.preventDefault();
        //llamamos a la validacion de campo
        validacion();
    });

});