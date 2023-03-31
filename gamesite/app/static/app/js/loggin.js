// Set the initial value of the isAdmin variable
var isAdmin = false;

// Function to update the visibility of the span element
function updateSpanVisibility() {
  if (isAdmin) {
    $("#admin-dd").removeClass("d-none");
  } else {
    $("#admin-dd").addClass("d-none");
  }
}
// Obtener el valor del elemento isAdmin del almacenamiento local cuando se carga la página
var isAdminItem = localStorage.getItem("isAdmin");
if (isAdminItem) {
  isAdmin = isAdminItem == "true";
}

updateSpanVisibility();

//Se ejecuta el document.ready para que primero cargue el documento
// y una vez que cargue completamente, se ejecutara js
$(document).ready(function () {
    $("#mensaje").hide();
    alert("Para iniciar sesion:    USUARIO --> admin    CONTRASEÑA --> admin");
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
            isAdmin = true;
            // Establecer el valor del elemento isAdmin en el almacenamiento local
            localStorage.setItem("isAdmin", isAdmin);
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
        let redireccionar = validacion();
        updateSpanVisibility();
        //Si la validacion es correcta
        if (redireccionar) {
            //mandar alerta de inicio de sesion exitoso y que será redireccionado
            alert("Inicio de sesion exitoso, sera redireccionado a la pagina principal");
            window.location.href = "../index.html";
            }
    });
});
