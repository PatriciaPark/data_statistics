window.onload = function () {
    defaultYear();
}
// 연도 데이터 입력
function defaultYear() {
    const now = new Date();
    const currentYear = now.getFullYear();
    document.getElementById("yearSearch").value = year;
}

// jQuery
// 연도 변경시 데이터 변경
$("#yearSearch").on("propertychange change keyup input click", function() {
    $("#selectForm").submit();
});

// Generate Report (PDF)
function CreatePDFfromHTML() {
    var HTML_Width = $(".container-fluid").width();
    var HTML_Height = $(".container-fluid").height();
    var top_left_margin = 15;
    var PDF_Width = HTML_Width + (top_left_margin * 2);
    var PDF_Height = (PDF_Width * 1.5) + (top_left_margin * 2);
    var canvas_image_width = HTML_Width;
    var canvas_image_height = HTML_Height;

    var totalPDFPages = Math.ceil(HTML_Height / PDF_Height) - 1;

    html2canvas($(".container-fluid")[0]).then(function (canvas) {
        var imgData = canvas.toDataURL("image/jpeg", 1.0);
        var pdf = new jsPDF('p', 'pt', [PDF_Width, PDF_Height]);    // 가로출력: 'p' -> 'l'

        pdf.addImage(imgData, 'JPG', top_left_margin, top_left_margin, canvas_image_width, canvas_image_height);
        for (var i = 1; i <= totalPDFPages; i++) { 
            pdf.addPage(PDF_Width, PDF_Height);
            pdf.addImage(imgData, 'JPG', top_left_margin, -(PDF_Height*i)+(top_left_margin*4),canvas_image_width,canvas_image_height);
        }
        pdf.save("Dashboard_"+ year + ".pdf");
    });
}
