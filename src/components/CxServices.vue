<template>
  <section class="services" id="services">
    <div class="container">
      <h2 class="section-title">Nuestros Servicios</h2>
      <div class="services-list">
        <div class="service" v-for="(service, index) in services" :key="index">
          <h3 class="service-title">{{ service.title }}</h3>
          <p class="service-description">{{ service.description }}</p>
          <button class="cta-button">Conocer más</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "CxServices",
  data() {
    return {
      services: [
        {
          title: "Terapia Reiki",
          description: "Descripción breve de la terapia Reiki.",
        },
        {
          title: "Masaje Holístico",
          description: "Descripción breve del masaje holístico.",
        },
        {
          title: "Aromaterapia",
          description: "Descripción breve de la aromaterapia.",
        },
        // Añadir más servicios según sea necesario
      ],
    };
  },
};
</script>
<style scoped>
.services {
  background-color: var(--color-background);
  color: var(--color-text);
  padding: 2rem 1rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.section-title {
  text-align: center;
  font-family: var(--font-homenaje);
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.services-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.service {
  background-color: var(--color-primary);
  border-radius: 5px;
  margin-bottom: 1rem;
  padding: 1rem;
  text-align: center;
  width: 100%;
  max-width: 600px; /* Para limitar el ancho de las cards */
}

.service-title {
  font-family: var(--font-sans);
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.service-description {
  font-family: var(--font-sans);
  font-size: 1rem;
  margin-bottom: 1rem;
}

.cta-button {
  background-color: var(--color-accent);
  border: none;
  border-radius: 5px;
  color: var(--color-text);
  padding: 0.5rem 1rem;
  font-size: 1rem;
  cursor: pointer;
}

@media (min-width: 768px) {
  .services-list {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
  }

  .service {
    width: 48%;
    max-width: none; /* Eliminar la limitación de ancho en pantallas grandes */
  }
}
</style>
