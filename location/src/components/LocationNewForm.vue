<template>
    <div class="container mt-10 changeBG">
        <div class="row">
            <div class="col-md-5 d-flex align-items-center">
                <h1>Enregistrer votre nouvelle location.</h1>
            </div>
            <div class="col-md-6 offset-md-1">
                <form class="mt-4 mt-md-0" @submit="handleForm">
                    <div class="form-group">
                        <label for="numloc">Numero location</label>
                        <input type="text" v-model="location.numloc" class="form-control" id="name" required maxlength="5">
                    </div>
                    <div class="form-group">
                        <label for="nomloc">Nom location</label>
                        <input type="text" v-model="location.nom_loc" class="form-control" id="nomloc" required maxlength="25">
                    </div>
                    <div class="form-group">
                        <label for="designVoit">Quel voiture allez-vous prendre?</label>
                        <input type="text" v-model="location.design_voiture" class="form-control" id="designVoit" required maxlength="25">
                    </div>
                    <div class="form-group">
                        <label for="nbj">Combien de jour?</label>
                        <input type="text" v-model="location.nbr_jour" class="form-control" id="nbj" required inputmode="numeric" pattern="[0-9]*">
                    </div>
                    <div class="form-group">
                        <label for="txj">Pourquel tarif?</label>
                        <input type="text" v-model="location.taux_jour" class="form-control" id="txj" required inputmode="numeric" pattern="[0-9]*">
                    </div>
                    <div class="form-group">
                        <input type="submit" class="mt-2 btn btn-primary btn-lg" value="Enregistrer"/>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import $ from 'jquery';

import LocationDataService from '@/services/LocationDataServices';

export default {
    name: 'LocationNewForm',
    data(){
        return{
            location: {
                numloc: "",
                nom_loc: "",
                design_voiture: "",
                nbr_jour: "",
                taux_jour: "",
            }
        }
    },
    methods: {
        handleForm(e){
            e.preventDefault();
            this.saveLocation();
        },
        createLocation(){

        },
        saveLocation(){
            // const loc = {
            //     numloc: this.location.numloc,
            //     nom_loc: this.location.nom_loc,
            //     design_voiture: this.location.design_voiture,
            //     nbr_jour: this.location.nbr_jour,
            //     taux_jour: this.location.taux_jour
            // };

            // const { numloc, nom_loc, design_voiture, nbr_jour, taux_jour } = location;
            // const variable = { numloc, nom_loc, design_voiture, nbr_jour, taux_jour };


            LocationDataService.create(this.location)
                .then((response) => {
                    // redirection list
                    this.$router.push({name: 'list'})
                })
                .catch((error) => {
                    console.log(error);
                })

            this.setInput();

        },

        setInput(){
            this.location.numloc = ""
            this.location.nom_loc = ""
            this.location.design_voiture = ""
            this.location.nbr_jour = ""
            this.location.taux_jour = ""
        }
    },
    mounted() {
        $('.form-group').each((i, e) => {
            $('.form-control', e)
                .focus(function () {
                    e.classList.add('not-empty');
                })
                .blur(function () {
                    this.value === '' ? e.classList.remove('not-empty') : null;
                    // e.classList.add('not-empty');
                });
        });
    },
}

</script>

<style scoped>
h1 {
    font-weight: 900;
    /* text-transform: uppercase; */
    color: #25138a;
}

.form-control {
    border-radius: 0;
}

.form-control:focus {
    box-shadow: none;
}

.form-group {
    position: relative;
    margin-bottom: 25px;
}

.form-group>label {
    text-transform: uppercase;
    font-size: 10px;
    color: #a1a2a3;
    transform-origin: 0 0;
    transform: scale(1.4);
    pointer-events: none;
    position: relative;
    z-index: 5;
}

.form-group>input {
    width: 100%;
}

.form-group>label {
    transition: transform 0.4s;
    transform-origin: 0 0;
    transform: scale(1.4) translateY(20px);
}

.form-group.not-empty>label {
    transform: none;
}

.form-control {
    border: 0;
    border-bottom: 1px solid #a1a2a3;
}

.form-control,
.form-control:focus,
.form-control:focus:hover {
    color: #2b2828;
    background: none;
    outline: none;
}

.form-control:focus,
.form-control:focus:hover {
    border-bottom: 1px solid #25138a;
}
</style>

