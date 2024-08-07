<template>
  <div class="form-container" id="contact">
    <form>
      <input type="text" placeholder="Nombre" class="form-input" />
      <input type="email" placeholder="Correo electrónico" class="form-input" />
      <textarea placeholder="Mensaje" class="form-input"></textarea>
      <button type="submit" class="submit-button">Enviar</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "CxFooter",
};
</script>

<style scoped>
.form-container {
  width: 100%;
  max-width: 800px; /* 80% of 1000px for example */
  margin: 0 auto;
  padding: 1rem;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-input {
  width: 100%;
  max-width: 80%;
  margin-bottom: 1rem;
  padding: 0.5rem;
  border: 1px solid var(--color-text);
  border-radius: 5px;
  font-size: 1rem;
  color: var(--color-background);
  background-color: var(--color-text);
}

.submit-button {
  background-color: var(--color-primary);
  color: var(--color-text);
  border: none;
  border-radius: 5px;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  cursor: pointer;
}

@media (min-width: 768px) {
  .form-input {
    max-width: 80%;
  }
}
</style>
