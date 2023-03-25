let baseNav = document.getElementById("baseNav");
baseNav.innerHTML += `
<nav class="navbar navbar-expand-md navbar-dark bg-dark"
     style="padding-left:1rem">
  <a class="navbar-brand" href="../index.html">GameSite</a>
  <button
    class="navbar-toggler"
    type="button"
    data-bs-toggle="collapse"
    data-bs-target="#navbarNav"
    aria-controls="navbarNav"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item dropdown">
        <a
          class="nav-link dropdown-toggle active"
          href="#"
          role="button"
          data-bs-toggle="dropdown"
          aria-expanded="false"
        >
          Categorías
        </a>
        <ul class="dropdown-menu">
          <li>
            <a class   = "dropdown-item" href="terror.html">Terror</a>
          </li>
          <li>
            <a class   = "dropdown-item" href="guerra.html">Guerra</a>
          </li>
          <li>
            <a class   = "dropdown-item" href="aventura.html">Aventura</a>
          </li>
          <li><a class = "dropdown-item" href="rpg.html">RPG</a></li>
          <li>
            <a class   = "dropdown-item" href="plataforma.html">Plataforma</a>
          </li>
        </ul>
      </li>
      <li class="nav-item">
        <a class="nav-link active" href="formulario.html">Unete</a>
      </li>
    </ul>
    <ul class="navbar-nav ms-auto pe-2">
            <span class="d-none" id="admin-dd">
              <li class="nav-item dropdown">
                <a
                  class="nav-link dropdown-toggle"
                  href="#"
                  id="navbarDropdown"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                  >
                  ADMIN
                </a>
                <ul
                  class="dropdown-menu dropdown-menu-center"
                  aria-labelledby="navbarDropdown"
                  >
                  <li>
                    <a class="dropdown-item" href="#"
                      >Configuración de catalogo</a
                    >
                  </li>
                  <li>
                    <a class="dropdown-item" href="#">Analisis de datos</a>
                  </li>
                  <li>
                    <a class="dropdown-item" href="#">Monitorear usuarios</a>
                  </li>
                </ul>
              </li>
            </span>
      <li class="nav-item">
        <a class="nav-link active" href="loggin.html"><span id="admin-status"></span></a>
      </li>
    </ul>
  </div>
</nav>
`;
