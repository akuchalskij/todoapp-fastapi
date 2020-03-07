<template>
    <v-form
            lazy-validation
            ref="form"
            v-model="valid"
    >
        <v-alert type="success" v-if="successful">
            Published!
        </v-alert>

        <v-alert type="error" v-if="error">
            {{ errors }}
        </v-alert>

        <v-text-field
                :counter="10"
                label="Title"
                required
                v-model="title"
        ></v-text-field>

        <v-text-field
                label="Description"
                required
                v-model="description"
        ></v-text-field>

        <v-btn
                :disabled="!valid"
                @click="create"
                class="mr-4"
                color="success"
        >
            Submit
        </v-btn>
    </v-form>
</template>

<script>
    import {instance} from '../../main'

    export default {
        name: "Create",
        data() {
            return {
                valid: true,
                title: '',
                description: '',
                error: false,
                successful: false,
                errors: []
            };
        },
        methods: {
            async create() {
                const formData = {
                    "title": this.title,
                    "description": this.description
                };

                await instance
                    .post("tasks/", formData)
                    .then(() => {
                        this.successful = true;
                        this.error = false;
                        this.errors = [];
                        this.$refs.form.reset()
                    })
                    .catch(error => {
                        this.errors = error.response.data.detail;
                        this.successful = false;
                        this.error = true;
                    });
            }
        }

    }

</script>

<style scoped>

</style>