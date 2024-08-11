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
@import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,400;0,700;1,100;1,400;1,700&display=swap");

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
  --font-homenaje: "Poppins", sans-serif;
  --font-sans: "Poppins", sans-serif;
}

body {
  font-family: var(--font-sans);
  color: var(--color-text);
  background-color: var(--color-background);
  line-height: 1.6;
  margin: 0;
  padding: 0;
}

/* Use Poppins Regular (default) for most text */
p,
li,
span,
body {
  font-family: var(--font-sans);
  font-weight: 400; /* Poppins Regular */
}

/* Use Poppins Bold for headings */
h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: var(--font-homenaje);
  font-weight: 700; /* Poppins Bold */
}
</style>
