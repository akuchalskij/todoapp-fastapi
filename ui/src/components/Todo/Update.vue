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
                @click="update"
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
        name: "Todo",
        mounted() {
            this.getTask();
        },
        props: {
            taskId: {
                type: Number,
                required: true
            }
        },
        data() {
            return {
                error: false,
                successful: false,
                errors: [],
                valid: true,
                title: '',
                description: '',
            };
        },
        methods: {
            async update() {
                let title = this.title;
                let description = this.description;

                await instance
                    .put('tasks/' + this.taskId, {title, description})
                    .then(() => {
                        this.successful = true;
                        this.error = false;
                        this.errors = [];
                    })
                    .catch(error => {
                        this.errors = error.response.data.detail;
                        this.successful = false;
                        this.error = true;
                    });
            },
            async getTask() {
                await instance.get('/tasks/' + this.taskId).then(response => {
                    this.title = response.data.title;
                    this.description = response.data.description;
                });
            }
        }
    }
</script>

<style scoped>

</style>