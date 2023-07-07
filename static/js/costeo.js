let botonCalcular=document.querySelector(".boton-calcular");
let mlPresentacion=document.querySelector("#mlPresentacion");
let precioPresentacion=document.querySelector("#precioPresentacion");
let mlReceta=document.querySelector("#mlReceta");

let costo=document.querySelector("#costo");

botonCalcular.addEventListener("click", ()=>{
    //Declaro variables y casteo los valores dados por usuario
    let mlPres=parseFloat(mlPresentacion.value);
    let mlRec=parseFloat(mlReceta.value);
    let precioPres=parseFloat(precioPresentacion.value);

    //Calculo el costo de los ml del ingrediente
    let precioRec=(mlRec*precioPres)/mlPres;
    console.log("el precio calculado" + precioRec);
    
    //Actualizo el valor de costo
    costo.innerHTML=`
        <h2>Costo de los ml de la receta:  $${precioRec.toFixed(2)}</h2>
    `;

});

const reiniciar=()=>{
    location.reload();
};