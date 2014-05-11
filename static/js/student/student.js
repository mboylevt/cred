/**
 * Created by matt on 1/18/14.
 */

var options = [
        set0 = ['Option 1','Option 2'],
        set1 = ['First Option','Second Option','Third Option']
    ];

function makeUL(array) {
    var list = document.createElement('ul');

    for(var i = 0; i < array.length; i++) {
        var item = document.createElement('li');
//        var h2 = document.createElement('h2');
//        h2.appendChild(document.createTextNode(array[i]));
        item.appendChild(document.createTextNode(array[i]));
        list.appendChild(item);
    }
    return list;
}

$(function() {
    $('#student-search').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_student/search', {
        firstName: $('input[name="first-name"]').val()
      }, function(data) {
        document.getElementById('student-result').appendChild(makeUL(data.result));
      });
      return false;
    });
});

function populateDropdown(data) {
    var select = document.getElementById("student-dropdown");
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
      url: "/_student/get_students",
      context: document.body
    }).done(function(data) {
      populateDropdown(data.result);
    });
    console.log( "ready!" );
});

