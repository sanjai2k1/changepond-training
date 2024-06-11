function checkData(){
    // window.alert("hii")
    let uid = document.getElementById("userId").value
    let regex =  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&^])[A-Za-z\d@.#$!%*?&]{8,15}$/;

    if (uid.trim()===""){
        // window.alert("uid is required")
        document.getElementById("uiderror").innerHTML="uid required"
        document.getElementById("uiderror").style.color="red"
    }else if(!uid.trim().match("^[a-zA-z]{3,}$")){
        document.getElementById("uiderror").innerHTML="uid must be in proper format"
        document.getElementById("uiderror").style.color="red"

    }
    else{
                document.getElementById("uiderror").innerHTML=""
    }

    let upass = document.getElementById("password").value
    if(upass.trim()===""){
        document.getElementById("upasserror").innerHTML="Password required"
         document.getElementById("upasserror").style.color="red"
    }
    else if(!upass.trim().match(regex)){
         document.getElementById("upasserror").innerHTML="Password must be in proper format"
         document.getElementById("upasserror").style.color="red"
    }
    else{
         document.getElementById("upasserror").innerHTML=""
    }

}
