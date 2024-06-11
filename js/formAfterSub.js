
function checkAll(){
  let ufname = document.myform.fname.value
  let regex = "^[a-zA-Z]{3,15}$"
  let uedu = document.myform.uedu
  console.log(uedu)
  if(ufname.trim()===""){
    window.alert("This field is required")
    return false;
  }
  if(!ufname.trim().match(regex)){
    window.alert("enter range 3-15")
    return false;
  }
  if(uedu[0].checked==false &&uedu[0].checked==false &&uedu[0].checked==false &&uedu[0].checked==false ){
    window.alert("select your qualification")
    return false;
  }
}