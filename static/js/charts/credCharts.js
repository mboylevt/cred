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

function populateRadarChart() {
    var data = {
        labels : ["Eating","Drinking","Sleeping","Designing","Coding","Partying","Running"],
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
    var ctx = document.getElementById("studentRadarChart").getContext("2d");
    var myNewChart = new Chart(ctx).Radar(data);
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