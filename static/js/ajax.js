$(function(){
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


function likes(event, user, record) {

    if(user != "AnonymousUser"){
      var element = document.getElementById("Sample");
      var element2 = document.getElementById("LikeMain");
      if(element.className == 'watashi1'){
        /* default mode */
        console.log('Default Mode. -> Clicked Mode.')
        /*element2.add("active");*/
        element.className = 'watashi2';
        document.getElementById( "Sample" ).innerHTML =
          parseInt( document.getElementById( "Sample" ).firstChild.nodeValue ) + 1;
      }else{
        /* clicked mode */
        console.log("Clicked Mode. -> Default Mode.")
        /*element2.remove("active");*/
        element.className = 'watashi1';
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

        /*
        クリックしたら、classを変更
        この変更に応じて、colorとカウントを変える。

        */
    } else {
        window.location.href = '/accounts/login/';
        alert("'いいね'を押すためには、ログインが必要です。");
    }
}
