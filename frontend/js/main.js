$( document ).ready(function() {

    var dataPoints = [];
    var chart;
    $.getJSON("http://localhost/Hackathon/backend/soundData.json", function(data) {
        $.each(data, function(key, value){
            dataPoints.push({x: data.x, y: data.y});
            console.log(data.x);
            console.log(data.y)
        });
        chart = new CanvasJS.Chart("chartContainer",{
            title:{
                text:"Live Volume Chart"
            },
            data: [{
                type: "line",
                dataPoints : dataPoints,
            }]
        });
        chart.render();
        updateChart();
    });
    function updateChart() {
        $.getJSON("http://localhost/Hackathon/backend/soundData.json", function(data) {
            $.each(data, function(key, value) {
                dataPoints.push({
                    x: data.x,
                    y: data.y
                });
            });
            chart.render();
            setTimeout(function(){updateChart()}, 1000);
        });
    }
});
