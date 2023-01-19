window.onload = function () {
    searchStrReview();
}

// select box 선택시 로컬스토리지 저장 : store location
function selectedLoc() {
    localStorage.setItem("user_selected_loc", document.getElementById("selectSearchLoc").value);
    // location 정보 변환시 city/store 정보는 reset
    document.getElementById("selectSearchCity").value = "";
    localStorage.removeItem("user_selected_city");
    document.getElementById("selectSearchStr").value = "";
    localStorage.removeItem("user_selected_str");
    document.getElementById("selectForm").submit();
}

// select box 선택시 로컬스토리지 저장 : store city
function selectedCity() {
    localStorage.setItem("user_selected_city", document.getElementById("selectSearchCity").value);
    // location 정보 변환시 store 정보는 reset
    document.getElementById("selectSearchStr").value = "";
    localStorage.removeItem("user_selected_str");
    document.getElementById("selectForm").submit();
}

// select box 선택시 로컬스토리지 저장 : store name
function selectedStr() {
    localStorage.setItem("user_selected_str", document.getElementById("selectSearchStr").value);
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