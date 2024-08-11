<template>
  <div class="form-container" id="contact">
    <h2>Reserva tu sesión</h2>
    <div id="hubspot-form"></div>
  </div>
</template>

<script>
export default {
  name: "CxContactForm",
  mounted() {
    // Cargar el script de HubSpot
    const script = document.createElement("script");
    script.charset = "utf-8";
    script.type = "text/javascript";
    script.src = "//js.hsforms.net/forms/embed/v2.js";

    script.onload = () => {
      // Crear el formulario de HubSpot después de que se haya cargado el script
      window.hbspt.forms.create({
        region: "na1",
        portalId: "44184354",
        formId: "f7e45c1e-0f89-4383-b10b-b6d3b7da95d0",
        target: "#hubspot-form",
        onFormSubmit: () => {
          // Opcionalmente, puedes añadir una función aquí para manejar algo cuando el formulario se envíe.
        },
      });
    };

    // Agregar el script al cuerpo del documento
    document.body.appendChild(script);
  },
};
</script>

<style scoped>
.form-container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  padding: 1rem;
  margin-top: 5rem;
}

h2 {
  text-align: center;
  padding: 0.5rem;
  color: var(--color-primary);
}

#hubspot-form {
  width: 100%;
  max-width: 80%;
  margin: 0 auto;
}

.hs-form {
  text-align: center;
}

.hs-main-font-element {
  font-size: 1.2rem;
  color: var(--color-text);
}

.hs-form input[type="submit"] {
  background-color: var(--color-accent);
  color: var(--color-background);
  padding: 0.8rem 2rem;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.hs-form input[type="submit"]:hover {
  background-color: darken(var(--color-accent), 10%);
}

.hs-form .submitted-message {
  font-size: 1.5rem;
  color: var(--color-text);
  text-align: center;
  margin-top: 2rem;
}
</style>
