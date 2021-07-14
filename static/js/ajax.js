function likes(event, user, record) {
    if(user != "AnonymousUser"){
      var element = document.getElementById("Sample");
      var element2 = document.getElementById("LikeMain");
      if(element.className == 'watashi1'){
        element.className = 'watashi2';
        element2.className = 'btn1';
        document.getElementById( "Sample" ).innerHTML =
          parseInt( document.getElementById( "Sample" ).firstChild.nodeValue ) + 1;
      }else{
        element.className = 'watashi1';
        element2.className = 'btn2';
        document.getElementById( "Sample" ).innerHTML =
          parseInt( document.getElementById( "Sample" ).firstChild.nodeValue ) - 1;
      }
        fetch(myurl.base + 'likes/' + user + '/' + record, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json; charset=utf-8",
                    "X-CSRFToken": Cookies.get('csrftoken'),
                },
            body: JSON.stringify({"status": "requested by javascript."})
            }
        );
    } else {
        window.location.href = '/accounts/login/';
        alert("'いいね'を押すためには、ログインが必要です。");
    }
}
$(function(){
  console.log(user)
  if(user != "AnonymousUser"){
  $('.btn').on('click', function(event){
      event.preventDefault();
      $(this).toggleClass('active');

      if($(this).hasClass('active')){
          var text = $(this).data('text-clicked');
      } else {
          var text = $(this).data('text-default');
      }
      $(this).html(text);
  });
  };
});
