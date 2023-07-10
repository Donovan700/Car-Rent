<template>
    <p> Data : {{ myData }}</p>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ShowData',
    data(){
        return{
            myData: {}
        }
    },
    created(){

        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/location/create/',
        data:{
            numloc: 'lc-7',
            nom_loc: 'Fianara-Ivato',
            design_voiture: '206',
            nbr_jour: 10,
            taux_jour: 10000
        }
        })
        .then( (response) => {
            // this.myData = response.data
            console.log("Element add");
        })
        .catch((error) => {
            console.log(error);
        });

    }
}


</script>