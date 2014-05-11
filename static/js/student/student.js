/**
 * Created by matt on 1/18/14.
 */

function populateDropdown(data) {
    var select = document.getElementById("studentDropdown");
    var keys = Object.keys(data);
    for(var i = 0; i < keys.length; i++) {
        var key = keys[i];
        var opt = data[key];
        var el = document.createElement("option");
        el.textContent = opt;
        el.value = opt;
        select.appendChild(el);
    }
}

// A $( document ).ready() block.
$( document ).ready(function() {
    $.ajax({
      url: "/_student/get_student_names",
      context: document.body
    }).done(function(data) {
      populateDropdown(data.result);
    });
    populateLineChart();
    populateRadarChart();
    populatePieChart();
    console.log( "ready!" );
});

