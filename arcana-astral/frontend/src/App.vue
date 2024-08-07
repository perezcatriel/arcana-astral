<template>
  <VxHome />
</template>

<script>
import VxHome from './views/VxHome.vue'

export default {
  name: 'App',
  components: {
    VxHome
  }
}
</script>

<style>
/* Reset CSS */
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  scroll-behavior: smooth;
}

/* Global styles */
:root {
  --color-primary: #12c2e9;
  --color-accent: #8e95ed;
  --color-text: #f0f4fa;
  --color-background: #070412;
  --font-homenaje: "Sacramento", sans-serif;
  --font-sans: "Source Sans 3", sans-serif;
}

body {
  font-family: var(--font-sans);
  color: var(--color-text);
  background-color: var(--color-background);
  line-height: 1.6;
  margin: 0;
  padding: 0;
}

/* Mobile-first default styles for all components */
.header, .nav, .main, .footer {
  padding: 1rem;
}

/* Responsive adjustments for desktop */
@media (min-width: 768px) {
  .header {
    padding: 2rem;
  }
  .nav {
    padding: 2rem;
  }
  .main {
    padding: 2rem;
  }
  .footer {
    padding: 2rem;
  }
}
</style>
