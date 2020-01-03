function js1() {
   	alert("Hello from js1");
	axios.get("https://api.triptocarbon.xyz/v1/footprint?activity=10&activityType=miles&country=usa&mode=taxi")
    .then(function (response) {
        console.log(response.data);
        document.getElementById("textConsumo").innerHTML = response.data;
    })
    .catch(function (error) {
        console.log(error);
    });
}