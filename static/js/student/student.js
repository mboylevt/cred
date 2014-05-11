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
        el.value = key;
        select.appendChild(el);
    }
}

function refreshData() {
    var dropdown = document.getElementById("studentDropdown");
    var studentId = dropdown.options[dropdown.selectedIndex].value;
    console.log('Selected: ' + studentId);
    $.ajax({
      url: "/_student/get_cred_points_by_type",
      context: document.body,
      data: {studentId : studentId}
    }).done(function(data) {
      populateRadarChart(data.result);
    });
    $.ajax({
      url: "/_student/get_cred_points_by_class",
      context: document.body,
      data: {studentId : studentId}
    }).done(function(data) {
      populateBarChart(data.result);
    });
}

// A $( document ).ready() block.
$( document ).ready(function() {
    $.ajax({
      url: "/_student/get_student_names",
      context: document.body
    }).done(function(data) {
      populateDropdown(data.result);
    });
    console.log( "ready!" );
});

