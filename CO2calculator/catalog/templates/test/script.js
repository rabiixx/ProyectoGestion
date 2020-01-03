$.getJSON('https://api.triptocarbon.xyz/v1/footprint?activity=10&activityType=miles&country=usa&mode=taxi', function (response) {
        console.log(response.data);
    })
    .catch(function (error) {
        console.log(error);
    });