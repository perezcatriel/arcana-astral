<template>
  <header class="header">
    <div class="container">
      <div class="logo-container">
        <img src="@/assets/logo.png" alt="Arcana Astral Logo" class="logo-image" />
      </div>
      <h1 class="logo">Arcana Astral</h1>
      <button class="menu-toggle" @click="toggleMenu">
        &#9776;
      </button>
      <nav class="nav" :class="{ 'nav-open': isMenuOpen }">
        <ul>
          <li><a href="#services">Servicios</a></li>
          <li><a href="#testimonials">Testimonios</a></li>
          <li><a href="#contact">Contacto</a></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: "CxHeader",
  data() {
    return {
      isMenuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
};
</script>

<style scoped>
.header {
  background-color: var(--color-background);
  color: var(--color-text);
  padding: 1rem;
  position: relative;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.logo-container {
  position: absolute;
  left: 1rem;
  top: 1rem;
}

.logo-image {
  width: 50px;
  height: auto;
  border-radius: 50%;
}

.logo {
  font-family: var(--font-homenaje);
  font-size: 1.5rem;
  margin: 0.5rem 0;
  text-align: center;
}

.menu-toggle {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 2rem;
  color: var(--color-text);
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  z-index: 2;
}

.nav {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background-color: var(--color-background);
  padding: 1rem;
  z-index: 10;
}

.nav-open {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav li {
  margin: 0.5rem 0;
}

.nav a {
  color: var(--color-text);
  text-decoration: none;
}

@media (min-width: 768px) {
  .container {
    flex-direction: column;
    align-items: center;
  }

  .logo-container {
    position: static;
    margin-bottom: 1rem;
  }

  .logo {
    font-size: 2rem;
    margin: 1rem 0;
    order: 1;
    text-align: center;
  }

  .menu-toggle {
    display: none;
  }

  .nav {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: static;
    width: auto;
    background: none;
    padding: 0;
    margin-top: 0.5rem;
  }

  .nav ul {
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding: 0;
    margin: 0;
  }

  .nav li {
    margin: 0 1rem;
  }
}
</style>
