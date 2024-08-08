<template>
  <div id="app">
    <VxHome />
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import VxHome from "./views/VxHome.vue";

export default {
  name: "App",
  components: {
    VxHome,
  },
};
</script>

<style>
/* Reset CSS */
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* Global styles */
:root {
  --color-primary: #b59788;
  --color-accent: #86553e;
  --color-text: #0c0907;
  --color-background: #eedcd4;
  --font-homenaje: "Homenaje", sans-serif;
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
.header,
.nav,
.main,
.footer {
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
