$.ajax({
    url: "py/progress.py",
    type: "post",
    datatype:"json",
    success: function(response){
      document.getElementById( 'pg' ).value = response.progress;
    }
  });
