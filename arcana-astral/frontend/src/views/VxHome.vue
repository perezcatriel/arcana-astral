<template>
  <div>
    <CxHeader />
    <CxHero />
    <CxServices />
    <CxTestimonials />
    <CxContactForm />
    <CxFooter />
  </div>
</template>

<script>
import CxHeader from '@/components/CxHeader.vue';
import CxHero from '@/components/CxHero.vue';
import CxServices from '@/components/CxServices.vue';
import CxTestimonials from '@/components/CxTestimonials.vue';
import CxContactForm from '@/components/CxContactForm.vue';
import CxFooter from '@/components/CxFooter.vue';

export default {
  name: 'VxHome',
  components: {
    CxHeader,
    CxHero,
    CxServices,
    CxTestimonials,
    CxContactForm,
    CxFooter,
  },
};
</script>

<style scoped>
/* Añade estilos específicos para la vista si es necesario */
</style>
