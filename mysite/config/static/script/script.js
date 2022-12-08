// open side menu area
function openNav() {
    document.getElementById("mySidenav").style.width = "20%";
    document.getElementById("main").style.marginLeft = "20%";
}

// 외부영역 클릭 시 close side menu 
document.onclick = function (e) {
    if (e.target.id != "sideMenu") {
        document.getElementById("mySidenav").style.width = "0";
        document.getElementById("main").style.marginLeft = "0";
    }
};