<template>
    <div v-if="appartment">
      <p><strong>Title:</strong> {{ appartment.title }}</p>
      <p><strong>Content:</strong> {{ appartment.content }}</p>
      <p><strong>Author:</strong> {{ appartment.author.username }}</p>
  
      <div v-if="user.id === appartment.author.id">
        <p><router-link :to="{name: 'EditAppartment', params:{id: appartment.id}}" class="btn btn-primary">Edit</router-link></p>
        <p><button @click="removeAppartment()" class="btn btn-secondary">Delete</button></p>
      </div>
    </div>
  </template>
  
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Appartment',
    props: ['id'],
    async created() {
      try {
        await this.viewAppartment(this.id);
      } catch (error) {
        console.error(error);
        this.$router.push('/dashboard');
      }
    },
    computed: {
      ...mapGetters({ appartment: 'stateAppartment', user: 'stateUser'}),
    },
    methods: {
      ...mapActions(['viewAppartment', 'deleteAppartment']),
      async removeAppartment() {
        try {
          await this.deleteAppartment(this.id);
          this.$router.push('/dashboard');
        } catch (error) {
          console.error(error);
        }
      }
    },
  });
  </script>
  