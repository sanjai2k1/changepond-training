import { Component } from '@angular/core';
import { FormGroup,FormControl,Validators } from '@angular/forms';
@Component({
  selector: 'app-rtf',
  templateUrl: './rtf.component.html',
  styleUrl: './rtf.component.css'
})
export class RtfComponent {

userform:any
ngOnInit(){
  this.userform = new FormGroup({
    fname:new FormControl("",[Validators.required,Validators.pattern("^[a-zA-Z]{3,15}$")]),
    password:new FormControl("",[Validators.required,Validators.pattern("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")]) ,
    email:new FormControl("",[Validators.required,Validators.pattern("[A-Za-z0-9\._%+\-]+@[A-Za-z0-9\.\-]+\.[A-Za-z]{2,}")]) ,
    term:new FormControl("",[Validators.required])
    })
}

getData(){
  console.log(this.userform.value)
}



}
