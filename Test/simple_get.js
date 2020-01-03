alert("Hello from js1");

axios.get('https://api.triptocarbon.xyz/v1/footprint?activity=10&activityType=miles&country=usa&mode=taxi').then(resp => {
    console.log(resp.data);
});