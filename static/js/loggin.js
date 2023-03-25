//Se ejecuta el document.ready para que primero cargue el documento
// y una vez que cargue completamente, se ejecutara js
$(document).ready(function () {
    $("#mensaje").hide();
    //Funcion para reciclar mensajes
    const msg = (mensaje, type) => {
        if (type == "correcto") {
            $("#mensaje").html(mensaje);
            $("#mensaje").removeClass("incorrecto");
            $("#mensaje").addClass("correcto");
            $("#mensaje").show();
        } else {
            $("#mensaje").html(mensaje);
            $("#mensaje").removeClass("correcto");
            $("#mensaje").addClass("incorrecto");
            $("#mensaje").show();
        };
    };
    //Funcion para validar el Loggin
    const validacion = () => {
        //Creamos las variables
        const usuario_in = $("#usuario").val();
        const contrasenia_in = $("#contrasenia").val();
        let flag = false;
        //Validacion
        if (usuario_in == "admin" && contrasenia_in == "admin") {
            //Mensaje correcto
            msg("Inicio de session exitoso.", "correcto");
            flag = true;
        } else if ($.trim(usuario_in) == "" || usuario_in == null) {
            //Mensaje incorrecto campo usuario vacio
            msg("El nombre de usuario no puede estar vacio", "incorrecto");
        } else if ($.trim(contrasenia_in) == "" || contrasenia_in == null) {
            //Mensaje incorrecto campo contraseña vacio
            msg("La contraseña no puede estar vacia", "incorrecto");
        } else {
            //Mensaje incorrecto
            msg("Usuario y/o contraseña invalido<br>Intente nuevamente", "incorrecto");
        };
        return flag;
    };
    //Boton de ingresar
    $("#ingresar").click(function (e) {
        //Detenemos el evento `Submit` para que no envie los datos aun
        e.preventDefault();
        //llamamos a la validacion de campo
        validacion();
    });
});