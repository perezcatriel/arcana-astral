<template>
  <footer class="footer">
    <div class="container">
      <p>© 2024 Arcana Astral. Todos los derechos reservados.</p>
      <div class="social-links">
        <a href="https://instagram.com/arcana.astral" class="social-link" target="_blank">
          <img src="@/assets/instagram.svg" alt="Instagram" class="social-logo" />
        </a>
      </div>
      <p class="credits">
        Creado por <a href="https://datacraft.vercel.app" target="_blank" class="credit-link">DataCraft</a>
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "CxFooter",
};
</script>

<style scoped>
.footer {
  background-color: var(--color-background);
  color: var(--color-text);
  padding: 1rem;
  text-align: center;
}

.social-links {
  margin-top: 1rem;
}

.social-link {
  color: var(--color-text);
  margin: 0 0.5rem;
  text-decoration: none;
}

.social-logo {
  width: 64px;
  height: 64px;
}

.credits {
  margin-top: 1rem;
}

.credit-link {
  color: var(--color-accent);
  text-decoration: none;
}


@media (min-width: 768px) {
  .social-links {
    display: flex;
    justify-content: center;
  }
}
</style>
