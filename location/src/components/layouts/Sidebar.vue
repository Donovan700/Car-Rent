<template>
    <div class="container-fluid">
    <div class="row flex-nowrap">
        <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
            <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-100">
                <RouterLink to="/" class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-white text-decoration-none">
                    <span class="fs-5 d-none d-sm-inline">Location</span>
                </RouterLink>
                <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start" id="menu">
                    <li class="nav-item">
                        <RouterLink to="/" class="nav-link align-middle px-0">
                            <i class="fs-4 bi-house"></i> <span class="ms-1 d-none d-sm-inline">Home</span>
                        </RouterLink>
                    </li>
                    <li>
                        <RouterLink to="/list" class="nav-link px-0 align-middle">
                            <i class="fs-4 bi-table"></i> <span class="ms-1 d-none d-sm-inline">List</span>
                        </RouterLink>
                    </li>
                    <li>
                        <RouterLink to="/form" class="nav-link px-0 align-middle">
                            <i class="fs-4 bi-people"></i> <span class="ms-1 d-none d-sm-inline">Add</span> 
                        </RouterLink>
                    </li>
                </ul>
            </div>
        </div>
        <div class="col">
            <RouterView/>
        </div>
    </div>
</div>

</template>

<script>

import {RouterLink, RouterView} from 'vue-router';
// import Welcome from '../Welcome.vue';

export default{
    name: "Sidebar",
    components:{
    }
}

</script>