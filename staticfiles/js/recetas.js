const { createApp } = Vue;
const cocktailApi = "https://sheetdb.io/api/v1/d3ovz969szcpn";
const idApp = "main-container";

const appRecetas = {
    data: function() {
        return{
            recetas: [],
        };
    },

    created: function() {
        fetch(cocktailApi)
            .then((res) => res.json())
            .then((recetasDesdeApi) => {console.log(recetasDesdeApi); this.recetas = recetasDesdeApi});
    },
};

const app = createApp(appRecetas);

app.mount(`#${idApp}`);