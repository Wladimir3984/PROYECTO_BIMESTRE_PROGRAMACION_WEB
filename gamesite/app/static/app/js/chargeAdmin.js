// Set the initial value of the isAdmin variable
var isAdmin = false;

// Function to update the visibility of the span element
function updateSpanVisibility() {
  if (isAdmin) {
    $("#admin-dd").removeClass("d-none");
    $("#admin-status").html("Cerrar sesión");
    // Agregar un controlador de eventos click al elemento a
    $("#admin-status").closest("a").click(function(event) {
      // Evitar que el enlace siga su comportamiento predeterminado
      event.preventDefault();

      // Borrar el almacenamiento local
      localStorage.clear();

      // Redirigir a la página de inicio de sesión

      // Obtener la ruta actual
      var currentPath = window.location.pathname;

      // Construir la ruta a la página de inicio de sesión
      var loginPath;
      if (currentPath.includes("/templates/")) {
        loginPath = "loggin.html";
      } else {
        loginPath = "templates/loggin.html";
      }
      //window.location.href = loginPath;
    });
  } else {
    $("#admin-dd").addClass("d-none");
    $("#admin-status").html("Iniciar sesión");
  }
}
// Obtener el valor del elemento isAdmin del almacenamiento local cuando se carga la página
var isAdminItem = localStorage.getItem("isAdmin");
if (isAdminItem) {
  isAdmin = isAdminItem == "true";
}

updateSpanVisibility();
