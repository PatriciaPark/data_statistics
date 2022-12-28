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

// excel download
function fnExceldown(id, title){
    var tab_text = '<html xmlns:x="urn:schemas-microsoft-com:office:excel">';
    tab_text = tab_text + '<head><meta http-equiv="content-type" content="application/vnd.ms-excel; charset=UTF-8">';
    tab_text = tab_text + '<xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet>'
    tab_text = tab_text + '<x:Name>Test Sheet</x:Name>';
    tab_text = tab_text + '<x:WorksheetOptions><x:Panes></x:Panes></x:WorksheetOptions></x:ExcelWorksheet>';
    tab_text = tab_text + '</x:ExcelWorksheets></x:ExcelWorkbook></xml></head><body>';
    tab_text = tab_text + "<table border='1px'>";
    var exportTable = $('#' + id).clone();
    exportTable.find('input').each(function (index, elem) { $(elem).remove(); });
    tab_text = tab_text + exportTable.html();
    tab_text = tab_text + '</table></body></html>';
    var data_type = 'data:application/vnd.ms-excel';
    var ua = window.navigator.userAgent;
    var msie = ua.indexOf("MSIE ");

    var fileName = title + '_' + prdData + '_' + yearDate + '.xls';
    //Explorer 환경에서 다운로드
    if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./)) {
        if (window.navigator.msSaveBlob) {
            var blob = new Blob([tab_text], {
                type: "application/csv;charset=utf-8;"
            });
            navigator.msSaveBlob(blob, fileName);
        }
    } else {
        var blob2 = new Blob([tab_text], {
            type: "application/csv;charset=utf-8;"
        });
        var filename = fileName;
        var elem = window.document.createElement('a');
        elem.href = window.URL.createObjectURL(blob2);
        elem.download = filename;
        document.body.appendChild(elem);
        elem.click();
        document.body.removeChild(elem);
    }
}