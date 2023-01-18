// Global Variables
let flag = -1;
// Onload
window.onload = function () {
    // Search area select box settings
    searchStrReview();
    // disabled Update Button
    document.getElementById("btnUpdate").disabled = true;
    // Store Info first-select click event for second select box
    if(flag < 0) {
        document.getElementById("first-select").click();
        flag = 1;
    }
}
// click reset button event
function resetForm() {
    document.getElementById("selectSearchLoc").value = "all";
    document.getElementById("selectSearchCity").value = "all";
    localStorage.removeItem("user_selected_loc");
    localStorage.removeItem("user_selected_city");
    document.getElementById("selectForm").submit();
}
// select box 선택시 local-storage 저장 : store location
function selectedLoc() {
    localStorage.setItem("user_selected_loc", document.getElementById("selectSearchLoc").value);
    // location 정보 변환시 city 정보는 reset
    document.getElementById("selectSearchCity").value = "";
    localStorage.removeItem("user_selected_city");
    document.getElementById("selectForm").submit();
}
// select box 선택시 local-storage 저장 : store city
function selectedCity() {
    localStorage.setItem("user_selected_city", document.getElementById("selectSearchCity").value);
    document.getElementById("selectForm").submit();
}
// Search area & Input area : select box settings
function searchStrReview() {
    // location
    if (!localStorage.getItem("user_selected_loc")) {
        document.getElementById("selectSearchLoc").value = "all";
    } else {
        document.getElementById("selectSearchLoc").value = localStorage.getItem("user_selected_loc");
        document.getElementById("first-select").value = localStorage.getItem("user_selected_loc");
    }
    // city
    if (!localStorage.getItem("user_selected_city")) {
        document.getElementById("selectSearchCity").value = "all";
    } else {
        document.getElementById("selectSearchCity").value = localStorage.getItem("user_selected_city");
        document.getElementById("second-select").value = localStorage.getItem("user_selected_city");
    }
}
// Update validation check
function updateField() {
    let value1 = document.getElementById("first-select").value
    let value2 = document.getElementById("second-select").value
    let value3 = document.getElementById("dataCode").value
    let value4 = document.getElementById("dataName").value
    if(value1 != '' && value2 != '' && value3 != '' && value4 != '') {
        alert("OK");
        return true;
    } else {
        alert("Please fill in all fields");
        return false;
    }
}
// jQuery Code
// select first select box value : change second select box value
$('#first-select').on("propertychange change keyup input click", function() {
    // send ajax request when the first select is changed:
    $.ajax({
      url : '/store/select/',
      type : 'GET',
      data : {
        location : $(this).val()
      },
      dataType: 'json',
      success : function(response) {
        // this function executes on receiving a successful response from the backend:
        var secondSelect = $('#second-select');
        secondSelect.empty();
  
        // iterate over the instances in the response and add them to the second select
        for (var instance in response.data) {
          secondSelect.append($('<option>', {
            value : response.data[instance].str_city,
            text : response.data[instance].str_city
          }));
        }
      }
    })
});
// click table Row : get & set values
$("#myTable tbody").on("click", "tr", function() { 	
    // clicked Row(<tr>)
    var td = $(this).children();
    
    // remove & add class for css (color and text effect at clicked row)
    $('.selected').removeClass('selected');
    td.attr("class", "selected");

    // get values with [td.eq(index)]
    var loc = td.eq(0).text();
    var city = td.eq(1).text();
    var code = td.eq(2).text();
    var name = td.eq(3).text();
    
    // set values at info field
    $("#first-select").val(loc);       
    $('#second-select').val(city);
    $("#dataCode").val(code);
    $("#dataName").val(name);

    // enabled Update Button
    $("#btnUpdate").prop('disabled', false);
});