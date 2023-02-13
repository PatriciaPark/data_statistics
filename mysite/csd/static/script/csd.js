//페이지 로드시 실행
window.onload=function(){
    searchDaily();
    baseGrid();
    localStorage.removeItem("user_selected_date");
}

// 파일 선택시에만 업로드 버튼 활성화
document.getElementById('fileInput').addEventListener('input', function(event) {
    document.getElementById('submitBtn').disabled = !this.value;
}, false);

// 파일 업로드시 로딩 애니메이션
document.getElementById('submitBtn').onclick = function (e) {
    var maskHeight = document.body.scrollHeight;
    document.getElementById('loading-div').style.display = '';
    document.getElementById('loading-div').style.height = maskHeight + 'px';
};

// 달력 날짜 선택시 로컬스토리지 저장
document.getElementById('monthSearch').addEventListener('input', function(event){
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
    const currentYear = yearData;
    const currentMonth = monthData;
    const updatedMonth = currentYear + "-" + currentMonth;
    document.getElementById('monthSearch').value = updatedMonth;
}

// Search 버튼 클릭이벤트 - 월별 데일리 데이터 출력    
function searchDaily() {
    // 검색창 달력 현재달/마지막선택달
    if(!localStorage.getItem("user_selected_date")) {
        if(!monthData) {
            defaultDate();
        } else {
            updatedDate();
        } 
    } else {
        document.getElementById('monthSearch').value = localStorage.getItem("user_selected_date");
    }
}

// 기본 그리드
function baseGrid() {
    // 테이블 th에 일 출력 (달력에 선택된 달의 마지막 일짜까지 출력) 
    const now = new Date();
    const monthSearch = document.getElementById('monthSearch').value;
    const lastDay = new Date( now.getFullYear(), ( monthSearch.substr(5)), 0 );
    const lastDate = lastDay.getDate(); // 해당 월의 마지막일자
    const thTr = document.getElementById('thTr');
    // total/average th
    const thT = document.createElement('th');
    const thA = document.createElement('th');
    // css를 위한 class 설정
    thT.setAttribute("class", "bg-gradient-primary");
    thA.setAttribute("class", "bg-gradient-primary");

    // 일자 출력
    for (hashDate = 0; hashDate < lastDate; hashDate++){
        let th = document.createElement('th');
        // css를 위한 class 설정
        th.setAttribute("class", "bg-gradient-primary");
        th.innerHTML = hashDate+1;
        thTr.append(th);
    }
    // total, average 출력
    thT.innerHTML = "Total";
    thTr.append(thT);
    thA.innerHTML = "Average";
    thTr.append(thA);    

    // 상품별 판매 데이터 출력
    prd11530035(lastDate);
    prd11060162(lastDate);
    prd17010087(lastDate);
    prd17010088(lastDate);
    prd17010004(lastDate);
    prd17010002(lastDate);
    prdlist();
}

function prd11530035(lastDate){
    // views.py에서 넘어온 상품별 데이터
    const prd11530035 = prd11530035Data.replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr = document.getElementById('tdTr');

    if(prd11530035.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td
        tdTotal.classList.add('setBold');
        tdAvg.classList.add('setBold');
        let total = 0;
        let count = 0;

        for (var i = 0; i < prd11530035.length/6; i++){
            // 판매량 td
            let td = document.createElement('td');
            // 상품코드, 바코드, 상품명, 일자별 판매량 데이터 출력
            if (i == 0) {
                tdCode.innerHTML = prd11530035[i*6+4];
                tdTr.append(tdCode);
                tdBar.innerHTML = prd11530035[i*6+3];
                tdTr.append(tdBar); 
                tdName.innerHTML = prd11530035[i*6+2];
                tdTr.append(tdName);
                td.innerHTML = prd11530035[i*6+5];
                tdTr.append(td);
                total += parseInt(prd11530035[i*6+5]);
                count ++;
            } else {
                // 해당 날짜 데이터가 있음
                if(prd11530035[i*6+5] != 0) {
                    td.innerHTML = prd11530035[i*6+5]-total;
                    tdTr.append(td);
                    total += parseInt(prd11530035[i*6+5]-total);
                    count ++;
                // 해당 날짜 데이터 없음
                } else {
                    td.innerHTML = 0;
                    tdTr.append(td);   
                }
            }
        }
        // 값
        tdTotal.innerHTML = total;
        tdTr.append(tdTotal);
        tdAvg.innerHTML = Math.round(total/count);
        tdTr.append(tdAvg);
    } else {
        // 데이터 없는 경우 No data 출력
        let td = document.createElement('td');
        td.colSpan = lastDate + 5;
        td.innerHTML = "No data: 正官庄活蔘２８Ｄ高麗蔘活 / 力飲１００ｍｌ＊１０瓶";
        tdTr.append(td);
    }
}

function prd11060162(lastDate){
    // views.py에서 넘어온 상품별 데이터
    const prd11060162 = prd11060162Data.replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr2 = document.getElementById('tdTr2');

    if(prd11060162.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td
        tdTotal.classList.add('setBold');
        tdAvg.classList.add('setBold');
        let total = 0;
        let count = 0;

        for (var i = 0; i < prd11060162.length/6; i++){
            // 판매량 td
            let td = document.createElement('td');      
            // 상품코드, 바코드, 상품명, 일자별 판매량 데이터 출력
            if (i == 0) {
                tdCode.innerHTML = prd11060162[i*6+4];
                tdTr2.append(tdCode);
                tdBar.innerHTML = prd11060162[i*6+3];
                tdTr2.append(tdBar); 
                tdName.innerHTML = prd11060162[i*6+2];
                tdTr2.append(tdName);
                td.innerHTML = prd11060162[i*6+5];
                tdTr2.append(td);
                total += parseInt(prd11060162[i*6+5]);
                count ++;
            } else {
                if(prd11060162[i*6+5] != 0) {
                    td.innerHTML = prd11060162[i*6+5]-total;
                    tdTr2.append(td);
                    total += parseInt(prd11060162[i*6+5]-total);
                    count ++;
                } else {
                    td.innerHTML = 0;
                    tdTr2.append(td);   
                }
            }
        }
        // 값
        tdTotal.innerHTML = total;
        tdTr2.append(tdTotal);
        tdAvg.innerHTML = Math.round(total/count);
        tdTr2.append(tdAvg);
    } else {
        // 데이터 없는 경우 No data 출력
        let td = document.createElement('td');
        td.colSpan = lastDate + 5;
        td.innerHTML = "No data: 正官庄高麗蔘精ＥＶＥＲＹ / ＴＩＭＥ－秘１０ｍｌ＊２０入";
        tdTr2.append(td);
    }
}

function prd17010087(lastDate){
    // views.py에서 넘어온 상품별 데이터
    const prd17010087 = prd17010087Data.replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr3 = document.getElementById('tdTr3');

    if(prd17010087.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td
        tdTotal.classList.add('setBold');
        tdAvg.classList.add('setBold');
        let total = 0;
        let count = 0;

        for (var i = 0; i < prd17010087.length/6; i++){
            // 판매량 td
            let td = document.createElement('td');      
            // 상품코드, 바코드, 상품명, 일자별 판매량 데이터 출력
            if (i == 0) {
                tdCode.innerHTML = prd17010087[i*6+4];
                tdTr3.append(tdCode);
                tdBar.innerHTML = prd17010087[i*6+3];
                tdTr3.append(tdBar); 
                tdName.innerHTML = prd17010087[i*6+2];
                tdTr3.append(tdName);
                td.innerHTML = prd17010087[i*6+5];
                tdTr3.append(td);
                total += parseInt(prd17010087[i*6+5]);
                count ++;
            } else {
                if(prd17010087[i*6+5] != 0) {
                    td.innerHTML = prd17010087[i*6+5]-total;
                    tdTr3.append(td);
                    total += parseInt(prd17010087[i*6+5]-total);
                    count ++;
                } else {
                    td.innerHTML = 0;
                    tdTr3.append(td);   
                }
            }
        }
        // 값
        tdTotal.innerHTML = total;
        tdTr3.append(tdTotal);
        tdAvg.innerHTML = Math.round(total/count);
        tdTr3.append(tdAvg);
    } else {
        // 데이터 없는 경우 No data 출력
        let td = document.createElement('td');
        td.colSpan = lastDate + 5;
        td.innerHTML = "No data: 預購正官庄活蔘２８Ｄ高麗 / 蔘活力飲禮盒１００ｍｌ＊８入";
        tdTr3.append(td);
    }
}

function prd17010088(lastDate){
    // views.py에서 넘어온 상품별 데이터
    const prd17010088 = prd17010088Data.replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr4 = document.getElementById('tdTr4');

    if(prd17010088.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td
        tdTotal.classList.add('setBold');
        tdAvg.classList.add('setBold');
        let total = 0;
        let count = 0;

        for (var i = 0; i < prd17010088.length/6; i++){
            // 판매량 td
            let td = document.createElement('td');      
            // 상품코드, 바코드, 상품명, 일자별 판매량 데이터 출력
            if (i == 0) {
                tdCode.innerHTML = prd17010088[i*6+4];
                tdTr4.append(tdCode);
                tdBar.innerHTML = prd17010088[i*6+3];
                tdTr4.append(tdBar); 
                tdName.innerHTML = prd17010088[i*6+2];
                tdTr4.append(tdName);
                td.innerHTML = prd17010088[i*6+5];
                tdTr4.append(td);
                total += parseInt(prd17010088[i*6+5]);
                count ++;
            } else {
                if(prd17010088[i*6+5] != 0) {
                    td.innerHTML = prd17010088[i*6+5]-total;
                    tdTr4.append(td);
                    total += parseInt(prd17010088[i*6+5]-total);
                    count ++;
                } else {
                    td.innerHTML = 0;
                    tdTr4.append(td);   
                }
            }
        }
        // 값
        tdTotal.innerHTML = total;
        tdTr4.append(tdTotal);
        tdAvg.innerHTML = Math.round(total/count);
        tdTr4.append(tdAvg);
    } else {
        // 데이터 없는 경우 No data 출력
        let td = document.createElement('td');
        td.colSpan = lastDate + 5;
        td.innerHTML = "No data: 預購正官庄高麗蔘石榴飲 / ５０ｍｌ＊９入";
        tdTr4.append(td);
    }
}

function prd17010004(lastDate){
    // views.py에서 넘어온 상품별 데이터
    const prd17010004 = prd17010004Data.replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr5 = document.getElementById('tdTr5');

    if(prd17010004.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td
        tdTotal.classList.add('setBold');
        tdAvg.classList.add('setBold');
        let total = 0;
        let count = 0;

        for (var i = 0; i < prd17010004.length/6; i++){
            // 판매량 td
            let td = document.createElement('td');      
            // 상품코드, 바코드, 상품명, 일자별 판매량 데이터 출력
            if (i == 0) {
                tdCode.innerHTML = prd17010004[i*6+4];
                tdTr5.append(tdCode);
                tdBar.innerHTML = prd17010004[i*6+3];
                tdTr5.append(tdBar); 
                tdName.innerHTML = prd17010004[i*6+2];
                tdTr5.append(tdName);
                td.innerHTML = prd17010004[i*6+5];
                tdTr5.append(td);
                total += parseInt(prd17010004[i*6+5]);
                count ++;
            } else {
                if(prd17010004[i*6+5] != 0) {
                    td.innerHTML = prd17010004[i*6+5]-total;
                    tdTr5.append(td);
                    total += parseInt(prd17010004[i*6+5]-total);
                    count ++;
                } else {
                    td.innerHTML = 0;
                    tdTr5.append(td);   
                }
            }
        }
        // 값
        tdTotal.innerHTML = total;
        tdTr5.append(tdTotal);
        tdAvg.innerHTML = Math.round(total/count);
        tdTr5.append(tdAvg);
    } else {
        // 데이터 없는 경우 No data 출력
        let td = document.createElement('td');
        td.colSpan = lastDate + 5;
        td.innerHTML = "No data: 預購正官庄高麗蔘野櫻莓飲";
        tdTr5.append(td);
    }
}

function prd17010002(lastDate){
    // views.py에서 넘어온 상품별 데이터
    const prd17010002 = prd17010002Data.replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr6 = document.getElementById('tdTr6');

    if(prd17010002.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td
        tdTotal.classList.add('setBold');
        tdAvg.classList.add('setBold');
        let total = 0;
        let count = 0;

        for (var i = 0; i < prd17010002.length/6; i++){
            // 판매량 td
            let td = document.createElement('td');      
            // 상품코드, 바코드, 상품명, 일자별 판매량 데이터 출력
            if (i == 0) {
                tdCode.innerHTML = prd17010002[i*6+4];
                tdTr6.append(tdCode);
                tdBar.innerHTML = prd17010002[i*6+3];
                tdTr6.append(tdBar); 
                tdName.innerHTML = prd17010002[i*6+2];
                tdTr6.append(tdName);
                td.innerHTML = prd17010002[i*6+5];
                tdTr6.append(td);
                total += parseInt(prd17010002[i*6+5]);
                count ++;
            } else {
                if(prd17010002[i*6+5] != 0) {
                    td.innerHTML = prd17010002[i*6+5]-total;
                    tdTr6.append(td);
                    total += parseInt(prd17010002[i*6+5]-total);
                    count ++;
                } else {
                    td.innerHTML = 0;
                    tdTr6.append(td);   
                }
            }
        }
        // 값
        tdTotal.innerHTML = total;
        tdTr6.append(tdTotal);
        tdAvg.innerHTML = Math.round(total/count);
        tdTr6.append(tdAvg);
    } else {
        // 데이터 없는 경우 No data 출력
        let td = document.createElement('td');
        td.colSpan = lastDate + 5;
        td.innerHTML = "No data: 預購正官庄高麗蔘精ＥＶＥ / ＲＹＴＩＭＥ１０ｍｌ＊３０入";
        tdTr6.append(td);
    }
}    

function prdlist() {
    const prdlist = prdlistData.replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr7 = document.getElementById('tdTr7');

    if(prdlist.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td
        tdTotal.classList.add('setBold');
        tdAvg.classList.add('setBold');
        let total = 0;
        let count = 0;
        for (var i = 0; i < prdlist.length/6; i++){
            // 판매량 td
            let td = document.createElement('td');
            // 상품코드, 바코드, 상품명, 일자별 판매량 데이터 출력
            if (i == 0) {
                tdCode.innerHTML = prdlist[i*6+4];
                tdTr7.append(tdCode);
                tdBar.innerHTML = prdlist[i*6+3];
                tdTr7.append(tdBar); 
                tdName.innerHTML = prdlist[i*6+2];
                tdTr7.append(tdName);
                td.innerHTML = prdlist[i*6+5];
                tdTr7.append(td);
                total += parseInt(prdlist[i*6+5]);
                count ++;
            } else {
                // 해당 날짜 데이터가 있음
                if(prdlist[i*6+5] != 0) {
                    td.innerHTML = prdlist[i*6+5]-total;
                    tdTr7.append(td);
                    total += parseInt(prdlist[i*6+5]-total);
                    count ++;
                // 해당 날짜 데이터 없음
                } else {
                    td.innerHTML = 0;
                    tdTr7.append(td);   
                }
            }
        }
        // 값
        tdTotal.innerHTML = total;
        tdTr7.append(tdTotal);
        tdAvg.innerHTML = Math.round(total/count);
        tdTr7.append(tdAvg);
    }
}