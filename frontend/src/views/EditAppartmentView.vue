<template>
    <section>
      <h1>Edit appartment</h1>
      <hr/><br/>
  
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" name="title" v-model="form.title" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Content:</label>
          <textarea
            name="content"
            v-model="form.content"
            class="form-control"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'EditAppartment',
    props: ['id'],
    data() {
      return {
        form: {
          title: '',
          content: '',
        },
      };
    },
    created: function() {
      this.GetAppartment();
    },
    computed: {
      ...mapGetters({ appartment: 'stateAppartment' }),
    },
    methods: {
      ...mapActions(['updateAppartment', 'viewAppartment']),
      async submit() {
      try {
        let appartment = {
          id: this.id,
          form: this.form,
        };
        await this.updateAppartment(appartment);
        this.$router.push({name: 'Appartment', params:{id: this.appartment.id}});
      } catch (error) {
        console.log(error);
      }
      },
      async GetAppartment() {
        try {
          await this.viewAppartment(this.id);
          this.form.title = this.appartment.title;
          this.form.content = this.appartment.content;
        } catch (error) {
          console.error(error);
          this.$router.push('/dashboard');
        }
      }
    },
  });
  </script>
  