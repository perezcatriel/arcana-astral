<template>
  <section class="testimonials" id="testimonials">
    <div class="container">
      <h2 class="section-title">Testimonios</h2>
      <div class="testimonial-list">
        <div
          class="testimonial"
          v-for="(testimonial, index) in testimonials"
          :key="index"
        >
          <p class="testimonial-text">{{ testimonial.text }}</p>
          <p class="testimonial-author">{{ testimonial.author }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "CxTestimonials",
  data() {
    return {
      testimonials: [
        {
          text: "Excelente experiencia, altamente recomendado.",
          author: "Juan Pérez",
        },
        {
          text: "Un cambio de vida, gracias Arcana Astral.",
          author: "María López",
        },
        // Añadir más testimonios según sea necesario
      ],
    };
  },
};
</script>
<style scoped>
.testimonials {
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

.testimonial-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  width: 100%;
}

.testimonial {
  background-color: var(--color-primary);
  border-radius: 5px;
  padding: 1rem;
  text-align: center;
  width: 100%;
  max-width: 600px;
  min-height: 150px; /* Ajusta esta altura según sea necesario */
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.testimonial-text {
  font-family: var(--font-sans);
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.testimonial-author {
  font-family: var(--font-sans);
  font-size: 0.875rem;
}

@media (min-width: 768px) {
  .testimonial-list {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
  }

  .testimonial {
    width: 48%;
    max-width: none;
  }
}
</style>
