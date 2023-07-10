import { createRouter, createWebHistory} from 'vue-router';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('@/components/Home.vue')
        },
        {
            path: '/list',
            name: 'list',
            component: () => import('@/components/LocationList.vue')
        },
        {
            path: '/form',
            name: 'create',
            component: () => import('@/components/LocationNewForm.vue')
        },
        {
            path: '/update/:id',
            name: 'update',
            component: () => import('@/components/LocationEdit.vue')
        },
    ]
})

export default router;