function searchURL(){
    var con = document.getElementById('afterSearch');
    var temp = document.getElementById('URL').value;
    var split = temp.split("=");
    var source = "https://www.youtube.com/embed/"+split[1];
    document.getElementById('source').src = source;
    
/*    alert(source);*/
    var el = document.getElementById('intro');
    el.remove();
    document.getElementById('source').src = source;
    con.style.display = 'block';
}

function openTab(evt, tabName){
    var nowtab = document.getElementsByClassName('tabButton');
    for(i=0; i<nowtab.length; i++){
        nowtab[i].className = nowtab[i].className.replace(" On",""); //현재 활성화된 탭 버튼 끄기
    }

    var tabResult = document.getElementsByClassName('tabResult');
    for(i=0; i<tabResult.length; i++){
        tabResult[i].style.display = 'none';
    }  //모든 탭 내용 끄기

    evt.currentTarget.className += " On"; //현재누른 탭버튼 켜기
    document.getElementById(tabName).style.display = 'block'; //해당하는 탭 내용 켜기*/
}