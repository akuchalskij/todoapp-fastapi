<template>
    <v-app>
        <v-navigation-drawer app>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="title">
                        Todo App
                    </v-list-item-title>
                    <v-list-item-subtitle>
                        Python & VueJS
                    </v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

            <v-list dense nav>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon>mdi-view-dashboard</v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                        <v-list-item-title><router-link :to="{ name: 'read' }">Show all tasks</router-link></v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar
                app
                color="primary"
                dark
        >
            <v-spacer></v-spacer>
        </v-app-bar>

        <v-content class="app-container">
            <v-container fluid>

                <router-view></router-view>
                <v-card-text style="height: 100px; position: relative">
                    <router-link :to="{ name: 'create' }">
                        <v-btn
                                absolute
                                color="pink"
                                dark
                                fab
                                right
                                top
                        >
                            <v-icon>mdi-plus</v-icon>
                        </v-btn>
                    </router-link>
                </v-card-text>
            </v-container>

        </v-content>
        <v-footer app>
            <!-- -->
        </v-footer>
    </v-app>
</template>
<script>
    export default {
        name: 'App'
    }
</script>

<style>
    .app-container {
        height: 100vh;
    }
</style>
