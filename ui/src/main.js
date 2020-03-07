import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import axios from "axios";

import Create   from './components/Todo/Create'
import Read     from './components/Todo/Read'
import Update   from './components/Todo/Update'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/tasks',
            name: 'read',
            component: Read,
            props: true
        },
        {
            path: '/tasks/create',
            name: 'create',
            component: Create,
            props: true
        },
        {
            path: '/tasks/update',
            name: 'update',
            component: Update,
            props: true
        },
    ],
});


export const instance = axios.create({baseURL: 'http://localhost:8000/api/v1/'})

new Vue({
    render: h => h(App),
    vuetify,
    router
}).$mount('#app')
