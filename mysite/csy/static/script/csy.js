window.onload = function () {
    searchYearly();
    localStorage.removeItem("user_selected_year");
    localStorage.removeItem("user_selected_prd");
}

// 달력 날짜 선택시 로컬스토리지 저장
document.getElementById("yearSearch").addEventListener("input", function (event) {
    localStorage.setItem("user_selected_year", document.getElementById("yearSearch").value);
});

// select box 선택시 로컬스토리지 저장 : product name
function selectedPrd() {
    localStorage.setItem("user_selected_prd", document.getElementById("selectSearch").value);
}

// 검색창 달력 현재 연도로 디폴트 세팅
function defaultYear() {
    const now = new Date();
    const currentYear = now.getFullYear();
    document.getElementById("yearSearch").value = currentYear;
}

// 검색창 달력 데이터 업데이트한 달로 세팅
function updatedYear() {
    document.getElementById("yearSearch").value = yearDate;
}

// select box 데이터 업데이트한 값으로 세팅
function updateSelect() {
    document.getElementById("selectSearch").value = prdData;
}

function searchYearly() {
    // 검색창 달력 현재연도/마지막 선택연도
    if (!localStorage.getItem("user_selected_year")) {
        if (yearDate == "None" || !yearDate) {
            defaultYear();
        } else {
            updatedYear();
        }
    } else {
        document.getElementById("yearSearch").value = localStorage.getItem("user_selected_year");
    }

    // 검색창 select box 상품명 설정
    if (!localStorage.getItem("user_selected_prd")) {
        if(!prdData || prdData == "None") {
            document.getElementById("selectSearch").value = "11530035";
        } else {
            updateSelect();
        }
    } else {
        document.getElementById("selectSearch").value = localStorage.getItem("user_selected_prd");
    }
}