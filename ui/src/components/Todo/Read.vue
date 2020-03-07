<template>
    <v-simple-table>
        <template v-slot:default>
            <thead>
            <tr>
                <th class="text-left">ID</th>
                <th class="text-left">Title</th>
                <th class="text-left">Action</th>
            </tr>
            </thead>
            <tbody>
            <tr :key="task.id" v-for="task in tasks">
                <td>{{ task.id }}</td>
                <td>{{ task.title }}</td>
                <td>
                    <div class="actions">
                        <router-link :to="{ name: 'update', params: { taskId : task.id } }">
                            <v-btn class="mx-1" color="primary" dark fab small>
                                <v-icon dark>mdi-pencil</v-icon>
                            </v-btn>
                        </router-link>
                        <v-btn @click="deleteTask(task.id)" class="mx-1" color="red" dark fab small>
                            <v-icon dark>mdi-minus</v-icon>
                        </v-btn>
                    </div>
                </td>
            </tr>
            </tbody>
        </template>
    </v-simple-table>
</template>

<script>
    import {instance} from '../../main'

    export default {
        name: "Read",
        data() {
            return {
                tasks: {}
            };
        },
        mounted() {
            this.getTasks()
        },
        methods: {
            async getTasks() {
                await instance.get('tasks/').then(response => (this.tasks = response.data));
            },
            async deleteTask(id) {
                await instance.delete("tasks/" + id).then(response => {
                    console.log(response.data);
                    this.getTasks();
                });
            },
        }
    }

</script>

<style scoped>

</style>