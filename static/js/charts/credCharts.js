/**
 * Created by matt on 5/11/14.
 */

function populateRadarChart(result) {
    var pointsEarned = result['Earned'];
    var pointsMissed = result['Missed'];
    var options = {
                scaleOverlay : false,
                scaleOverride : true,
                scaleSteps : 10,
                scaleStepWidth : 4,
                scaleStartValue : 0
    };
    var chartData = {
        labels : ["Cooperation","Responsibility","Empowerment","Determination"],
        datasets : [
            {
                fillColor : "rgba(220,220,220,0.5)",
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                 data : [pointsMissed["C"],pointsMissed["R"],pointsMissed["E"],pointsMissed["D"]]
            },
            {
                fillColor : "rgba(151,187,205,0.5)",
                strokeColor : "rgba(151,187,205,1)",
                pointColor : "rgba(151,187,205,1)",
                pointStrokeColor : "#fff",
                data : [pointsEarned["C"],pointsEarned["R"],pointsEarned["E"],pointsEarned["D"]]
            }
        ]
    };
    var ctx = document.getElementById("studentRadarChart").getContext("2d");
    var myNewChart = new Chart(ctx).Radar(chartData,options);
}

function populateBarChart(result) {
    var pointsEarned = result['Earned'];
    var pointsMissed = result['Missed'];
    var keys = Object.keys(pointsEarned);
    var pointsMissedData = [];
    var pointsEarnedData = [];
    for (var key in keys) {
        pointsEarnedData.push(pointsEarned[keys[key]]);
        pointsMissedData.push(pointsMissed[keys[key]]);
    }
    var options = {
        scaleSteps : 20,
        scaleOverride : true,
        scaleStepWidth : 1,
        scaleStartValue : 0
    };

    var chartData = {
        labels : keys,
        datasets : [
            {
                fillColor : "rgba(220,220,220,0.5)",
                strokeColor : "rgba(220,220,220,1)",
                data : pointsMissedData
            },
            {
                fillColor : "rgba(151,187,205,0.5)",
                strokeColor : "rgba(151,187,205,1)",
                data : pointsEarnedData
            }
        ]
    };
    var ctx = document.getElementById("studentBarChart").getContext("2d");
    var myNewChart = new Chart(ctx).Bar(chartData,options);
}