<template>
    <div class="container-fluid">
        <LocationTable 
            :headerProp="headers" 
            :elementsProp="locations" 
            v-if="locations" 
            @deleteLocation="handleDelete"
            ref="locationTable"
        />

        <div class="container-fluid">
            <div class="row mt-4">
                <div class="col">Total loyer:</div>
                <div class="col"><b>{{ loyerTotal() }} Ar</b></div>
            </div>
            <div class="row mt-4">
                <div class="col">Loyer Max:</div>
                <div class="col"><b>{{ Math.max(...loyers) }} Ar</b></div>
            </div>
            <div class="row mt-4">
                <div class="col">Loyer Min:</div>
                <div class="col"><b>{{ Math.min(...loyers) }} Ar</b></div>
            </div>
            <!-- <div class="clearfix">
                <div class="hint-text">Total loyer:<b>{{ loyerTotal() }} Ar</b></div>
                <div class="hint-text">Loyer Max:<b>{{ Math.max(...loyers) }} Ar</b></div>
                <div class="hint-text">Loyer Min:<b>{{ Math.min(...loyers) }} Ar</b></div>
            </div> -->
        </div>
        
        
    </div>
</template>

<script>

import LocationDataService from '@/services/LocationDataServices';
import LocationTable from '@/components/LocationTable.vue';

export default{
    name: "LocationList",
    components:{
        LocationTable
    },
    data(){
        return{
            headers:[ "Numero location", "Designation", "Voiture", "Nombre de jours", "Tarif journalier", "Actions"],

            locations: null,

            loyers: [0]
        }
    },
    methods: {
        retrieveLocations(){
            LocationDataService.getAll()
                .then((response) =>{
                    
                    this.locations = response.data.map((e) => this.formatLocation(e));
                    console.log("Location :" +this.locations[1].nom_loc);

                    this.loyers = this.locations.map( (e) => e.taux_jour * e.nbr_jour )
                    // console.log(this.loyers);
                    // return an array of data
                })
                .catch((error)=>{
                    console.log("This "+ error);
                })

        },
        
        getLocation(id){
            LocationDataService.get(id)
            .then((response) => {
                this.currentLocation = response.data
                // console.log(this.currentLocation);
            })
            .catch((error) => {

                console.log("Id : "+id)
                console.error(error);
            })
        },
        handleDelete(id){

            LocationDataService.delete(id)
            .then((response) => {
                 // redirection list
                //  this.$router.push({name:'list'})
                // console.log("Element deleted succesfully");
                this.retrieveLocations();
                // console.log("New Location:");
                // console.log(this.locations);
            })
            .catch((error) => {
                console.log("Id : "+id)
                console.error(error);
            })

            
        },

        formatLocation(location){
            return{
                numloc: location.numloc,
                nom_loc: location.nom_loc,
                design_voiture: location.design_voiture,
                nbr_jour: location.nbr_jour,
                taux_jour: location.taux_jour
            }
        },
        loyerTotal(){
            let cum = 0;
            for(const e of this.loyers){
                cum += e;
            }
            return cum;
        }
    },
    mounted(){
        this.retrieveLocations();
    }
}
</script>


