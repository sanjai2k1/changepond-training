import { Component } from '@angular/core';
import { DatabaseServiceService } from '../../shared/service/database-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
uid:any
upass:any
userData:any=[]

constructor(private dbServ:DatabaseServiceService,private routerObj:Router){

}



signIn(){
  console.log(this.uid,this.upass)
  this.dbServ.getRecord("users").subscribe((res)=>{
    // console.log(res)
    this.userData=res
    let data = this.userData.filter((val:any)=>{
      return val.uname===this.uid && val.upass ===this.upass
    })
    if(data.length>0){
      sessionStorage.setItem("user",this.uid)
      this.routerObj.navigate(['maindashboard'])
    }else{
      window.alert("Wrong Credential inserted")
      this.uid=""
      this.upass="";
    }
  })
}
}
