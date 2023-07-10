<template>
    <!-- <div> -->
        <!-- <form>
            <div class="form-group">
                <label for="numLoc">Numero location</label>
                <input type="text" class="form-control" id="nomLoc" placeholder="ex: lc-1">
            </div>
            <div class="form-group">
                <label for="nomLoc">Nom location</label>
                <input type="text" class="form-control" id="nomLoc" placeholder="ex: Tana - Majunga">
            </div>
            <div class="form-group">
                <label for="designVoit">Designation voiture</label>
                <input type="text" class="form-control" id="designVoit" placeholder="ex: Sprinter">
            </div>
            <div class="form-group">
                <label for="nbj">Nombre de jour</label>
                <input type="number" class="form-control" id="nbj">
            </div>
            <div class="form-group">
                <label for="tj">Taux Journalier</label>
                <input type="number" class="form-control" id="tj">
            </div>
        </form> -->
    <!-- </div> -->


    <div style="display:flex;width:100%;">
        <form>
            <div style="width:100%;">
                <p>Numero location</p>
                <input type="text" autofocus>
            </div>
            <div style="width:100%;">
                <p>Nom Location</p>
                <input type="text">
            </div>

            <div style="width:100%;">
                <p>Voiture</p>
                <input type="text">
            </div>
            <div style="width:100%;">
                <p>Nombre de jours</p>
                <input type="number">
            </div>
            <div style="width:100%;">
                <p>Taux journalier</p>
                <input type="text">
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "LocationForm"
}
</script>

<style scoped>
   
   input:focus{
        outline: none;
    }
    
    form{
        width: 35%;
        margin-left:auto;
        margin-right:auto;
        padding:50px;
        background:whitesmoke;
        border-radius:5px;
        position:relative;
        font-family: 'Libre Franklin', sans-serif;
    }

    form > div {
        float:left;margin-bottom:30px;
    }
    form > div > p{
        font-size: 12px;margin-bottom: 3px;
    }
    form > div > input{
        font-size:12px;letter-spacing:1px;padding:  5px;border: 0;background:  whitesmoke;border-bottom: 1px solid silver;width: 100%;color: gray;
    }

    form > p:last-of-type{
        text-align: center;padding-top: 50px;display:  table;width: 100%;color:white;
    }

    form > p:last-of-type > a{
        cursor:pointer;border:0;
        padding: 10px 25px;
        background:  silver;
        border-radius:  28px;
        font-size: 12px; 
    }

    /* delete */
    form > a:last-of-type{
        position:absolute;
        bottom: 10px;
        right: 15px;
        font-size:  10px;
        letter-spacing:  1px;
        font-style: italic;
    }
</style>