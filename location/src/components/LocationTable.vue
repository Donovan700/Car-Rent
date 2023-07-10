<template>
    <div class="container-fluid">
        <div class="table-responsive">
            <div class="table-wrapper">
                <div class="table-title">
                    <div class="row">
                        <div class="col-sm-6">
                            <h2>Manage <b>Locations</b></h2>
                        </div>
                        <div class="col-sm-6">
                            <RouterLink to="/form" class="btn btn-success" data-toggle="modal"><i
                                    class="bi bi-plus-circle"></i> <span> Add New Location</span></RouterLink>
                        </div>
                    </div>
                </div>
                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th v-for="header in headers">{{ header }}</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="element in elements">
                            <td>{{ element.numloc }}</td>
                            <td>{{ element.nom_loc }}</td>
                            <td>{{ element.design_voiture }}</td>
                            <td>{{ element.nbr_jour }}</td>
                            <td>{{ element.taux_jour }} Ar</td>
                            <td>
                                <span class="edit" @click="handleEdit(element.numloc)"><i class="bi bi-pen" title="Edit"></i></span>
                                <span class="delete" @click="deleteLocation(element.numloc)"><i class="bi bi-trash3"
                                        title="Delete"></i></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <!-- <div class="clearfix">
                    <div class="hint-text">Number of locations: <b>{{ elements.length }}</b></div>
                </div> -->
            </div>
        </div>
    </div>
</template>

<script>

import { RouterLink } from 'vue-router';

import LocationDataService from '@/services/LocationDataServices';

export default {
    name: 'LocationTable',
    data() {
        return {
            headers: [],
            elements: [],
            currentLocation: {}
        }
    },
    props: {
        headerProp: {
            type: Array,
            required: true
        },
        elementsProp: {
            type: Array,
            required: true
        }
    },
    methods: {
        deleteLocation(id) {
            this.$emit('deleteLocation', id);
        },
        refresh() {
            this.headers = [...this.headerProp];
            this.elements = [...this.elementsProp];

            // console.log("Props update: ");
            // console.log(this.elementsProp);
            // console.log("Data update: ");
            // console.log(this.elements);
        },
        handleEdit(id){
            this.$router.push({name:'update',params:{id:id}})
        }
    },
    watch: {
        elementsProp: {
            immediate: true,
            handler(newVal) {
                this.headers = [...this.headerProp];
                this.elements = [...newVal];
                // console.log("Props wacth: ");
                // console.log(this.elementsProp);
                // console.log("Data watch: ");
                // console.log(this.elements);
            },
            deep: true
        }
    },
    created() {
        this.headers = [...this.headerProp];
        this.elements = [...this.elementsProp];
        // console.log("Props load: ");
        // console.log(this.elementsProp);
        // console.log("Data load: ");
        // console.log(this.elements);
    }
}

</script>

<style scoped>
.table-responsive {
    margin: 30px 0;
}

.table-wrapper {
    background: #fff;
    padding: 20px 25px;
    border-radius: 3px;
    min-width: 1000px;
    box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
}

.table-title {
    padding-bottom: 15px;
    background: #435d7d;
    color: #fff;
    padding: 16px 30px;
    min-width: 100%;
    margin: -20px -25px 10px;
    border-radius: 3px 3px 0 0;
}

.table-title h2 {
    margin: 5px 0 0;
    font-size: 24px;
}

.table-title .btn-group {
    float: right;
}

.table-title .btn {
    color: #fff;
    float: right;
    font-size: 13px;
    border: none;
    min-width: 50px;
    border-radius: 2px;
    border: none;
    outline: none !important;
    margin-left: 10px;
}

.table-title .btn i {
    float: left;
    font-size: 21px;
    margin-right: 5px;
}

.table-title .btn span {
    float: left;
    margin-top: 2px;
}

table.table tr th,
table.table tr td {
    border-color: #e9e9e9;
    padding: 12px 15px;
    vertical-align: middle;
}

table.table tr th:first-child {
    width: 60px;
}

table.table tr th:last-child {
    width: 100px;
}

table.table-striped tbody tr:nth-of-type(odd) {
    background-color: #fcfcfc;
}

table.table-striped.table-hover tbody tr:hover {
    background: #f5f5f5;
}

table.table th i {
    font-size: 13px;
    margin: 0 5px;
    cursor: pointer;
}

table.table td:last-child i {
    opacity: 0.9;
    font-size: 22px;
    margin: 0 5px;
}

table.table td a {
    font-weight: bold;
    color: #566787;
    display: inline-block;
    text-decoration: none;
    outline: none !important;
}

table.table td a:hover {
    color: #2196F3;
}

table.table td a.edit {
    color: #FFC107;
}

table.table td a.delete {
    color: #F44336;
}

table.table td i {
    font-size: 19px;
}

table.table .avatar {
    border-radius: 50%;
    vertical-align: middle;
    margin-right: 10px;
}

.hint-text {
    float: left;
    margin-top: 10px;
    font-size: 13px;
}
</style>