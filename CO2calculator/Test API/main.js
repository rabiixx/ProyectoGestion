/*const getBtn = document.getElementById('boton');

if(getBtn) { console.log("Not null") } else { console.log("Could be null") } // Could be null

for(let i = 0; null; i++) { console.log("Won't run") }

getBtn ? console.log("truthy value") : console.log("Falsy value") // falsy value*/

function js1() {
   	alert("Hello from js1");
	axios.get("https://api.triptocarbon.xyz/v1/footprint?activity=10&activityType=miles&country=usa&mode=taxi")
    .then(function (response) {
        console.log(response.data);
        //document.getElementById("textConsumo").innerHTML = response.data;
    })
    .catch(function (error) {
        console.log(error);
    });
}

/*getBtn.addEventListener("click", getData);*/