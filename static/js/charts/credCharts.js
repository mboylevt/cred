/**
 * Created by matt on 5/11/14.
 */

function populateLineChart() {
    var data = {
        labels : ["January","February","March","April","May","June","July"],
        datasets : [
            {
                fillColor : "rgba(220,220,220,0.5)",
                strokeColor : "rgba(220,220,220,1)",
                pointColor : "rgba(220,220,220,1)",
                pointStrokeColor : "#fff",
                data : [65,59,90,81,56,55,40]
            },
            {
                fillColor : "rgba(151,187,205,0.5)",
                strokeColor : "rgba(151,187,205,1)",
                pointColor : "rgba(151,187,205,1)",
                pointStrokeColor : "#fff",
                data : [28,48,40,19,96,27,100]
            }
        ]
    };
    //Get the context of the canvas element we want to select
    var ctx = document.getElementById("studentLineChart").getContext("2d");
    var myNewChart = new Chart(ctx).Line(data);
}

function populateRadarChart(result) {
    var chartData = 0;
    var options = 0;
    if (result) {
        var pointsEarned = result['Earned'];
        var pointsMissed = result['Missed'];
        console.log("Earned: " + pointsEarned);
        console.log("Missed: " + pointsMissed);
        options = {
                    scaleOverlay : false,
                    scaleOverride : true,
                    scaleSteps : 10,
                    scaleStepWidth : 4,
                    scaleStartValue : 0
        };
        chartData = {
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
    }
    else {
        chartData = {
            labels : ["Eating","Drinking","Sleeping","Designing","Coding","Partying","Running"],
//            labels : ["Eating","Drinking","Sleeping","Designing"],
            datasets : [
                {
                    fillColor : "rgba(220,220,220,0.5)",
                    strokeColor : "rgba(220,220,220,1)",
                    pointColor : "rgba(220,220,220,1)",
                    pointStrokeColor : "#fff",
                    data : [65,59,90,81,56,55,40]
                },
                {
                    fillColor : "rgba(151,187,205,0.5)",
                    strokeColor : "rgba(151,187,205,1)",
                    pointColor : "rgba(151,187,205,1)",
                    pointStrokeColor : "#fff",
                    data : [28,48,40,19,96,27,100]
                }
            ]
        };
    }
    var ctx = document.getElementById("studentRadarChart").getContext("2d");
    var myNewChart = new Chart(ctx).Radar(chartData,options);
}

function populatePieChart() {
    var data = [
        {
            value: 30,
            color:"#F38630"
        },
        {
            value : 50,
            color : "#E0E4CC"
        },
        {
            value : 100,
            color : "#69D2E7"
        }
    ];
    var ctx = document.getElementById("studentPieChart").getContext("2d");
    var myNewChart = new Chart(ctx).Pie(data);
}