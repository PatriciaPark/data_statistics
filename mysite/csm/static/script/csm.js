//페이지 로드시 실행
window.onload = function () {
    searchMonthly();
    searchStrReview();
}
// click reset button event
function resetForm() {
    document.getElementById("selectAddLoc").value = "all";
    document.getElementById("selectAddCity").value = "all";
    document.getElementById("selectAddStr").value = "all";
    document.getElementById("selectSearch").value = "";
    document.getElementById("selectSort").value = "";
    localStorage.removeItem("user_selected_loc");
    localStorage.removeItem("user_selected_city");
    localStorage.removeItem("user_selected_str");
    localStorage.removeItem("user_selected_date");
    localStorage.removeItem("user_selected_prd");
    localStorage.removeItem("user_selected_sort");
    document.getElementById("selectForm").submit();
}
// 파일 선택시에만 버튼 활성화
document.getElementById("fileInput").addEventListener("input", function (event) {
    document.getElementById("submitBtn").disabled = !this.value;
}, false);

// 파일 업로드시 로딩 애니메이션
document.getElementById("submitBtn").onclick = function (e) {
    loading();
};

// 달력 날짜 선택시 로컬스토리지 저장
document.getElementById("monthSearch").addEventListener("input", function (event) {
    localStorage.setItem("user_selected_date", document.getElementById("monthSearch").value);
});

// 로딩 화면 함수
function loading() {
    var maskHeight = document.body.scrollHeight;
    document.getElementById("loading-div").style.display = "";
    document.getElementById("loading-div").style.height = maskHeight + "px";
}

// select box 선택시 로컬스토리지 저장 : product name
function selectedPrd() {
    localStorage.setItem("user_selected_prd", document.getElementById("selectSearch").value);
}
// select box 선택시 로컬스토리지 저장 : sort
function selectedSort() {
    localStorage.setItem("user_selected_sort", document.getElementById("selectSort").value);
}
// select box 데이터 업데이트한 값으로 세팅
function updateSelect() {
    document.getElementById("selectSearch").value = prdData;
    document.getElementById("selectSort").value = sortData;
}

// 검색창 달력 현재 달로 디폴트 세팅
function defaultDate() {
    const now = new Date();
    const currentYear = now.getFullYear();
    const currentMonth = ("0" + (now.getMonth() + 1)).slice(-2);
    const defaultMonth = currentYear + "-" + currentMonth;
    document.getElementById("monthSearch").value = defaultMonth;
}

// 검색창 달력 데이터 업데이트한 달로 세팅
function updatedDate() {
    const currentYear = yearData;
    const currentMonth = monthData;
    const updatedMonth = currentYear + "-" + currentMonth;
    document.getElementById("monthSearch").value = updatedMonth;
}

// Search 버튼 클릭이벤트 - 월별 데이터 출력    
function searchMonthly() {
    // 검색창 달력 현재달/마지막선택달
    if (!localStorage.getItem("user_selected_date")) {
        if (!monthData) {
            defaultDate();
        } else {
            updatedDate();
        }
    } else {
        document.getElementById("monthSearch").value = localStorage.getItem("user_selected_date");
    }

    // 검색창 select box 상품명 설정
    if (!localStorage.getItem("user_selected_prd")) {
        if(!prdData || prdData == "None") {
            document.getElementById("selectSearch").value = "";
        } else {
            updateSelect();
        }
    } else {
        document.getElementById("selectSearch").value = localStorage.getItem("user_selected_prd");
    }

    // 검색창 select box 정렬 조건 설정 
    if (!localStorage.getItem("user_selected_sort")) {
        if(!sortData || sortData == "None") {
            document.getElementById("selectSort").value = "";
        } else {
            updateSelect();
        }
    } else {
        document.getElementById("selectSort").value = localStorage.getItem("user_selected_sort");
    }
}

// 검색창 지역 select box 설정
function searchStrReview() {
    // location
    if (localStorage.getItem("user_selected_loc")) {
        document.getElementById("selectAddLoc").value = localStorage.getItem("user_selected_loc");
    } else {
        document.getElementById("selectAddLoc").value = "all";
    }
    // city
    if (localStorage.getItem("user_selected_city")) {
        document.getElementById("selectAddCity").value = localStorage.getItem("user_selected_city");
    } else {
        document.getElementById("selectAddCity").value = "all";
    }
    // store
    if (localStorage.getItem("user_selected_str")) {
        document.getElementById("selectAddStr").value = localStorage.getItem("user_selected_str");
    } else {
        document.getElementById("selectAddStr").value = "all";
    }
}

// jQuery Code
// select first select box value : change second select box value
$('#selectAddLoc').on("propertychange change keyup input click", function() {
    // send ajax request when the first select is changed:
    $.ajax({
        url : '/csm/select/',
        type : 'GET',
        data : {
            location : $(this).val()
        },
        dataType: 'json',
        success : function(response) {
            // this function executes on receiving a successful response from the backend:
            localStorage.setItem("user_selected_loc", $('#selectAddLoc').val());
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
            localStorage.removeItem("user_selected_city");
            localStorage.removeItem("user_selected_str");
        }
    })
});
// select second select box value : change third select box value
$('#selectAddCity').on("propertychange change keyup input click", function() {
    $.ajax({
        url : '/csm/select2/',
        type : 'GET',
        data : {
            city : $(this).val()
        },
        dataType: 'json',
        success : function(response) {
            // this function executes on receiving a successful response from the backend:
            localStorage.setItem("user_selected_city", $('#selectAddCity').val());
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
            localStorage.removeItem("user_selected_str");
        }
    })
});

$('#selectAddStr').on("propertychange change keyup input click", function() {
    localStorage.setItem("user_selected_str", $('#selectAddStr').val());
});