window.onload = function () {
    dateSetting();
}

// 달력 날짜 선택시 로컬스토리지 저장
document.getElementById("datePicker").addEventListener("input", function (event) {
    localStorage.setItem("user_selected_date", document.getElementById("datePicker").value);
});

// 달력 날짜 default
function dateSetting() {
    if (!localStorage.getItem("user_selected_date")) {
        document.getElementById('datePicker').valueAsDate = new Date();
    } else {
        document.getElementById("datePicker").value = localStorage.getItem("user_selected_date");
    }
}

// click reset button event
function resetForm() {
    localStorage.removeItem("user_selected_date");
    document.getElementById('datePicker').valueAsDate = new Date();
    document.getElementById("selectForm").submit();
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