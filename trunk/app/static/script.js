$(document).ready(function(){

  /**
   * 
   */
  $('#login-submit').click(function(){
    var email = $("#login-email").val();
    var pass = $('#login-ref-code').val();
    
    $.post(
      '/en/auth/login',
      {
        'login' : email,
        'password' : pass,
        'remember' : 0
      }
    );
  })
  /* end of login-submit */

  /**
   * 
   */
  $("#datepicker").datepicker({
    showOn: "both",
    buttonImage: "/images/calendar.gif",
    buttonImageOnly: true,
    dateFormat: "yy-mm-dd",
  });
  
  $("#clickfocus").setFocus(num){
      if(num == 1){
        document.myForm.myTextArea1.focus();
      }else if(num == 2){
        document.myForm.myTextArea2.focus();
      }
    }

});
