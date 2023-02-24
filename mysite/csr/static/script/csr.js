window.onload = function () {
    searchStrReview();

    // Pop-up for adding new review
    var target = document.querySelectorAll('.btn_open');
    var btnPopClose = document.querySelectorAll('.pop_wrap .btn_close');
    var targetID;

    // open popup 팝업 열기
    for(var i = 0; i < target.length; i++){
        target[i].addEventListener('click', function(){
        targetID = this.getAttribute('href');
        document.querySelector(targetID).style.display = 'block';
        });
    }
    // close popup 팝업 닫기
    for(var j = 0; j < target.length; j++){
        btnPopClose[j].addEventListener('click', function(){
        this.parentNode.parentNode.style.display = 'none';
        });
    }
}
// click reset button event
function resetForm() {
    document.getElementById("selectSearchLoc").value = "all";
    document.getElementById("selectSearchCity").value = "all";
    document.getElementById("selectSearchStr").value = "all";
    localStorage.removeItem("user_selected_loc");
    localStorage.removeItem("user_selected_city");
    localStorage.removeItem("user_selected_str");
    document.getElementById("selectForm").submit();
}

// 검색창 select box 설정
function searchStrReview() {
    // location
    if (!localStorage.getItem("user_selected_loc")) {
        document.getElementById("selectSearchLoc").value = "all";
    } else {
        document.getElementById("selectSearchLoc").value = localStorage.getItem("user_selected_loc");
    }
    // city
    if (!localStorage.getItem("user_selected_city")) {
        document.getElementById("selectSearchCity").value = "all";
    } else {
        document.getElementById("selectSearchCity").value = localStorage.getItem("user_selected_city");
    }
    // store
    if (!localStorage.getItem("user_selected_str")) {
        document.getElementById("selectSearchStr").value = "all";
    } else {
        document.getElementById("selectSearchStr").value = localStorage.getItem("user_selected_str");
    }
}

// jQuery Code
// MAIN - select first select box value : change second select box value
$('#selectSearchLoc').on("propertychange change keyup input click", function() {
    // send ajax request when the first select is changed:
    $.ajax({
        url : '/csr/select/',
        type : 'GET',
        data : {
            location : $(this).val()
        },
        dataType: 'json',
        success : function(response) {
            // this function executes on receiving a successful response from the backend:
            localStorage.setItem("user_selected_loc", $('#selectSearchLoc').val());
            var secondSelect = $('#selectSearchCity');
            secondSelect.empty();
            secondSelect.append($('<option>', {
                value : 'all',
                text : 'City'
            }));
            var thirdSelect = $('#selectSearchStr').empty();
            thirdSelect.append($('<option>', {
                value : 'all',
                text : 'Store'
            }));
    
            // iterate over the instances in the response and add them to the second select
            for (var instance in response.data) {
                secondSelect.append($('<option>', {
                    value : response.data[instance].str_city,
                    text : response.data[instance].str_city
                }));
            }
            localStorage.removeItem("user_selected_city");
            localStorage.removeItem("user_selected_str");
        }
    })
});
// select second select box value : change third select box value
$('#selectSearchCity').on("propertychange change keyup input click", function() {
    $.ajax({
        url : '/csr/select2/',
        type : 'GET',
        data : {
            city : $(this).val()
        },
        dataType: 'json',
        success : function(response) {
            // this function executes on receiving a successful response from the backend:
            localStorage.setItem("user_selected_city", $('#selectSearchCity').val());
            var secondSelect = $('#selectSearchStr');
            secondSelect.empty();
            secondSelect.append($('<option>', {
                value : 'all',
                text : 'Store'
            }));
    
            // iterate over the instances in the response and add them to the second select
            for (var instance in response.data) {
                secondSelect.append($('<option>', {
                    value : response.data[instance].str_code,
                    text : response.data[instance].str_name
                }));
            }
            localStorage.removeItem("user_selected_str");
        }
    })
});
$('#selectSearchStr').on("propertychange change keyup input click", function() {
    localStorage.setItem("user_selected_str", $('#selectSearchStr').val());
});

// POPUP - select first select box value : change second select box value
$('#selectAddLoc').on("propertychange change keyup input click", function() {
    // send ajax request when the first select is changed:
    $.ajax({
        url : '/csr/select/',
        type : 'GET',
        data : {
            location : $(this).val()
        },
        dataType: 'json',
        success : function(response) {
            // this function executes on receiving a successful response from the backend:
            var secondSelect = $('#selectAddCity');
            secondSelect.empty();
            secondSelect.append($('<option>', {
                value : 'all',
                text : 'City'
            }));
            var thirdSelect = $('#selectAddStr').empty();
            thirdSelect.append($('<option>', {
                value : 'all',
                text : 'Store'
            }));
    
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
// select second select box value : change third select box value
$('#selectAddCity').on("propertychange change keyup input click", function() {
    $.ajax({
        url : '/csr/select2/',
        type : 'GET',
        data : {
            city : $(this).val()
        },
        dataType: 'json',
        success : function(response) {
            // this function executes on receiving a successful response from the backend:
            var secondSelect = $('#selectAddStr');
            secondSelect.empty();
            secondSelect.append($('<option>', {
                value : 'all',
                text : 'Store'
            }));
    
            // iterate over the instances in the response and add them to the second select
            for (var instance in response.data) {
                secondSelect.append($('<option>', {
                    value : response.data[instance].str_code,
                    text : response.data[instance].str_name
                }));
            }
        }
    })
});

$('#selectAddStr').on("propertychange change keyup input click", function() {
    localStorage.setItem("user_selected_str", $('#selectAddStr').val());
});