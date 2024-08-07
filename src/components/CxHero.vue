<template>
    <section class="hero">
      <div class="overlay"></div>
      <div class="container">
        <h2 class="hero-title">Bienvenido a Arcana Astral</h2>
        <p class="hero-description">
          Descubre nuestras terapias holísticas para tu bienestar.
        </p>
        <a href="https://wa.me/543541638060" class="cta-button" target="_blank">Reserva tu sesión</a>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: "CxHero",
  };
  </script>
  
  #### CSS
  ```css
  <style scoped>
  .hero {
    position: relative;
    background-image: url("@/assets/background.webp");
    background-size: cover;
    background-position: center;
    color: var(--color-text);
    padding: 2rem 1rem;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1;
  }
  
  .container {
    position: relative;
    z-index: 2;
  }
  
  .hero-title {
    font-family: var(--font-sans);
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
  }
  
  .hero-description {
    font-family: var(--font-sans);
    font-size: 1rem;
    margin-bottom: 1rem;
  }
  
  .cta-button {
    display: inline-block;
    background-color: var(--color-primary);
    border: none;
    border-radius: 5px;
    color: var(--color-text);
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    cursor: pointer;
    text-decoration: none;
  }
  
  @media (min-width: 768px) {
    .hero {
      height: 60vh;
    }
  
    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
  
    .hero-title {
      font-size: 2.5rem;
    }
  
    .hero-description {
      font-size: 1.25rem;
    }
  
    .cta-button {
      padding: 1rem 2rem;
      font-size: 1.25rem;
    }
  }
  </style>
  