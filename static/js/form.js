function check(){
  var input_univ = document.getElementById( "id_hospital_name" ).value ;
  if (input_univ == "病院"){
      alert("病院名を入力してください！");
      return false
  }
  else{
      return true;
  }
}
function setAlert(){
  const p1 = document.getElementById("testModal");
  p1.style.display ="none";
}
