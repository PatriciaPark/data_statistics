//페이지 로드시 실행
window.onload = function () {
    searchDaily();
    localStorage.removeItem("user_selected_date");
}

// 파일 선택시에만 버튼 활성화
document.getElementById('fileInput').addEventListener('input', function (event) {
    document.getElementById('submitBtn').disabled = !this.value;
}, false);

// 파일 업로드시 로딩 애니메이션
document.getElementById('submitBtn').onclick = function (e) {
    var maskHeight = document.body.scrollHeight;
    document.getElementById('loading-div').style.display = '';
    document.getElementById('loading-div').style.height = maskHeight + 'px';
};

// 달력 날짜 선택시 로컬스토리지 저장
document.getElementById('monthSearch').addEventListener('input', function (event) {
    localStorage.setItem("user_selected_date", document.getElementById('monthSearch').value);
});

// 검색창 달력 현재 달로 디폴트 세팅
function defaultDate() {
    const now = new Date();
    const currentYear = now.getFullYear();
    const currentMonth = ("0" + (now.getMonth() + 1)).slice(-2);
    const defaultMonth = currentYear + "-" + currentMonth;
    document.getElementById('monthSearch').value = defaultMonth;
}

// 검색창 달력 데이터 업데이트한 달로 세팅
function updatedDate() {
    const now = new Date();
    const currentYear = now.getFullYear();
    const currentMonth = monthData;
    const updatedMonth = currentYear + "-" + currentMonth;
    document.getElementById('monthSearch').value = updatedMonth;
}

// Search 버튼 클릭이벤트 - 월별 데이터 출력    
function searchDaily() {
    // 검색창 달력 현재달/마지막선택달
    if (!localStorage.getItem("user_selected_date")) {
        if (!monthData) {
            defaultDate();
        } else {
            updatedDate();
        }
    } else {
        document.getElementById('monthSearch').value = localStorage.getItem("user_selected_date");
    }
}