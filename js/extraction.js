$(document).ready(function(){
  $('#Progress_Loading').hide(); //첫 시작시 로딩바를 숨겨준다.
})
.ajaxStart(function(){
  $('#Progress_Loading').show(); //ajax실행시 로딩바를 보여준다.
})

$(function(){
  $('#bt').click(function(){
    var url_link=$('#URL').val();
    var datalist = {'url_list': url_link};
    var check_progress = setInterval(function(){$.ajax({
        url: "py/progress.py",
        type: "post",
        datatype:"json",
        success: function(response){
          document.getElementById( 'pg' ).value = response.progress;
          document.getElementById( 'percent' ).innerHTML = " " + response.progress + '%';
        }
      });}, 3500);
    $.ajax({
      url: "py/Crawling(cnt)_test.py",
      type: "post",
      datatype:"json",
      data: datalist,
      success: function(response){
        clearInterval(check_progress);
        document.getElementById( 'pg' ).value = 100;
        document.getElementById( 'percent' ).innerHTML = " 100%";
        alert("SUCCESS!!!");
      
        chartConfig.scaleX.values=response.time;
        chartConfig.series[0].values=response.values;
        chartConfig.scaleY.values=response.range;
        chart();
      },
      done: function(response){
        clearInterval(check_progress);
        alert("DONE!!!");
        chart();
      },
      error:function(request, status, error, response){
		      alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
          clearInterval(check_progress);
          chartConfig.scaleX.values=response.time;
          chartConfig.series[0].values=response.values;
          chartConfig.scaleY.values=response.range;
          chart();
        }
    });
  });
});
