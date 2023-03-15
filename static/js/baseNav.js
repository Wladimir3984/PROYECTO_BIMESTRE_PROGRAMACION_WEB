let baseNav = document.getElementById("baseNav");
baseNav.innerHTML += `
<nav class="navbar navbar-expand navbar-dark bg-dark">
  <a class="navbar-brand" href="index.html">GameSite</a>
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
            <a class="dropdown-item" href="terror.html">Terror</a>
          </li>
          <li>
            <a class="dropdown-item" href="guerra.html">Guerra</a>
          </li>
          <li>
            <a class="dropdown-item" href="aventura.html">Aventura</a>
          </li>
          <li><a class="dropdown-item" href="rpg.html">RPG</a></li>
          <li>
            <a class="dropdown-item" href="plataforma.html">Plataforma</a>
          </li>
        </ul>
      </li>
      <li class="nav-item">
        <a class="nav-link active" href="../../formulario.html">Unete</a>
      </li>
    </ul>
  </div>
</nav>
`;
