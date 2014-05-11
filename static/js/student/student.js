/**
 * Created by matt on 1/18/14.
 */

function populateDropdown(data) {
    var select = document.getElementById("studentDropdown");
    for(var i = 0; i < data.length; i++) {
        var opt = data[i];
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
    console.log( "ready!" );
});

