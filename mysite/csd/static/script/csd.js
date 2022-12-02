window.onload=function(){
    searchDaily();
}

// 파일 선택시에만 버튼 활성화
document.getElementById('fileInput').addEventListener('input', function(event) {
    document.getElementById('submitBtn').disabled = !this.value;
}, false);

// Search 버튼 클릭이벤트 - 월별 데일리 데이터 출력    
function searchDaily() {
    // 검색창 달력 현재 달로 디폴트 세팅
    let now = new Date();
    let currentYear = now.getFullYear();
    let currentMonth = ("0" + (now.getMonth() + 1)).slice(-2);
    let defaultMonth = currentYear + "-" + currentMonth
    let monthSearch = document.getElementById('monthSearch').value;
    console.log(defaultMonth +" " + monthSearch);
    document.getElementById('monthSearch').value = defaultMonth;
    if(!monthSearch) {
    } else {
        document.getElementById('monthSearch').value = monthSearch
    }

    // 상품별 판매 데이터 출력
    prd11530035();
    prd11060162();
    prd17010087();
    prd17010088();
    prd17010004();
    prd17010002();

}

function prd11530035(){
    // views.py에서 넘어온 상품별 데이터
    const prd11530035 = "{{prd11530035}}".replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let thTr = document.getElementById('thTr');
    let tdTr = document.getElementById('tdTr');
    if(prd11530035.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td

        let thT = document.createElement('th');     // total th
        let thA = document.createElement('th');     // average th
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td
        
        for (var i = 0; i < prd11530035.length/6; i++){
            // 일자 출력
            let th = document.createElement('th');      // 일자 th
            let td = document.createElement('td');      // 판매량 td
            th.innerHTML = prd11530035[i*6+1].substr(8);
            thTr.append(th);
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
            } else {
                td.innerHTML = prd11530035[i*6+5]-prd11530035[(i-1)*6+5];
                tdTr.append(td);
            }
        }
        // total, average 출력
        thT.innerHTML = "Total";
        thTr.append(thT);
        thA.innerHTML = "Average";
        thTr.append(thA);
        // 값
        tdTotal.innerHTML = prd11530035[prd11530035.length-1];
        tdTr.append(tdTotal);
        tdAvg.innerHTML = (prd11530035[prd11530035.length-1])/(prd11530035.length/6);
        tdTr.append(tdAvg);
    }
}

function prd11060162(){
    // views.py에서 넘어온 상품별 데이터
    const prd11060162 = "{{prd11060162}}".replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr2 = document.getElementById('tdTr2');

    if(prd11060162.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td

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
            } else {
                td.innerHTML = prd11060162[i*6+5]-prd11060162[(i-1)*6+5];
                tdTr2.append(td);
            }
        }
        // 값
        tdTotal.innerHTML = prd11060162[prd11060162.length-1];
        tdTr2.append(tdTotal);
        tdAvg.innerHTML = (prd11060162[prd11060162.length-1])/(prd11060162.length/6);
        tdTr2.append(tdAvg);
    }
}

function prd17010087(){
    // views.py에서 넘어온 상품별 데이터
    const prd17010087 = "{{prd17010087}}".replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr3 = document.getElementById('tdTr3');

    if(prd17010087.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td

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
            } else {
                td.innerHTML = prd17010087[i*6+5]-prd17010087[(i-1)*6+5];
                tdTr3.append(td);
            }
        }
        // 값
        tdTotal.innerHTML = prd17010087[prd17010087.length-1];
        tdTr3.append(tdTotal);
        tdAvg.innerHTML = (prd17010087[prd17010087.length-1])/(prd17010087.length/6);
        tdTr3.append(tdAvg);
    }
}

function prd17010088(){
    // views.py에서 넘어온 상품별 데이터
    const prd17010088 = "{{prd17010088}}".replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr4 = document.getElementById('tdTr4');

    if(prd17010088.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td

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
            } else {
                td.innerHTML = prd17010088[i*6+5]-prd17010088[(i-1)*6+5];
                tdTr4.append(td);
            }
        }
        // 값
        tdTotal.innerHTML = prd17010088[prd17010088.length-1];
        tdTr4.append(tdTotal);
        tdAvg.innerHTML = (prd17010088[prd17010088.length-1])/(prd17010088.length/6);
        tdTr4.append(tdAvg);
    }
}

function prd17010004(){
    // views.py에서 넘어온 상품별 데이터
    const prd17010004 = "{{prd17010004}}".replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr5 = document.getElementById('tdTr5');

    if(prd17010004.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td

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
            } else {
                td.innerHTML = prd17010004[i*6+5]-prd17010004[(i-1)*6+5];
                tdTr5.append(td);
            }
        }
        // 값
        tdTotal.innerHTML = prd17010004[prd17010004.length-1];
        tdTr5.append(tdTotal);
        tdAvg.innerHTML = (prd17010004[prd17010004.length-1])/(prd17010004.length/6);
        tdTr5.append(tdAvg);
    }
}

function prd17010002(){
    // views.py에서 넘어온 상품별 데이터
    const prd17010002 = "{{prd17010002}}".replace(/\&#x27;|\{|\}|\s|\&lt;|\&gt;|\[|\]/g,'').split(/[:,]/);
    let tdTr6 = document.getElementById('tdTr6');

    if(prd17010002.length > 1) {
        let tdCode = document.createElement('td');  // 상품코드 td
        let tdBar = document.createElement('td');   // 바코드 td
        let tdName = document.createElement('td');  // 상품명 td
        let tdTotal = document.createElement('td'); // total td
        let tdAvg = document.createElement('td');   // average td

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
            } else {
                td.innerHTML = prd17010002[i*6+5]-prd17010002[(i-1)*6+5];
                tdTr6.append(td);
            }
        }
        // 값
        tdTotal.innerHTML = prd17010002[prd17010002.length-1];
        tdTr6.append(tdTotal);
        tdAvg.innerHTML = (prd17010002[prd17010002.length-1])/(prd17010002.length/6);
        tdTr6.append(tdAvg);
    }
}