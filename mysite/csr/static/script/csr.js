window.onload = function () {
    searchStrReview();
}

// select box 선택시 로컬스토리지 저장 : store location
function selectedLoc() {
    localStorage.setItem("user_selected_loc", document.getElementById("selectSearchLoc").value);
    document.getElementById("selectForm").submit();
}

// select box 선택시 로컬스토리지 저장 : store city
function selectedCity() {
    localStorage.setItem("user_selected_city", document.getElementById("selectSearchCity").value);
    document.getElementById("selectForm").submit();
}

// select box 선택시 로컬스토리지 저장 : store name
function selectedStr() {
    localStorage.setItem("user_selected_str", document.getElementById("selectSearchStr").value);
    document.getElementById("selectForm").submit();
}

function searchStrReview() {
    // 검색창 select box 설정
    if (!localStorage.getItem("user_selected_loc")) {
        document.getElementById("selectSearchLoc").value = "default";
    } else {
        document.getElementById("selectSearchLoc").value = localStorage.getItem("user_selected_loc");
    }
    if (!localStorage.getItem("user_selected_city")) {
        document.getElementById("selectSearchCity").value = "default";
    } else {
        document.getElementById("selectSearchCity").value = localStorage.getItem("user_selected_city");
    }
    if (!localStorage.getItem("user_selected_str")) {
        document.getElementById("selectSearchStr").value = "default";
    } else {
        document.getElementById("selectSearchStr").value = localStorage.getItem("user_selected_str");
    }
}