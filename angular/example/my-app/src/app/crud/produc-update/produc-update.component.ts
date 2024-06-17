import { Component } from '@angular/core';
import { DatabaseServiceService } from '../../shared/service/database-service.service';
import { ActivatedRoute, Router } from '@angular/router';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-produc-update',
  templateUrl: './produc-update.component.html',
  styleUrl: './produc-update.component.css'
})
export class ProducUpdateComponent {
  id:any
  prodData:any
  prodDataUpdate:any
constructor(private dbServ:DatabaseServiceService,private actRouteObj:ActivatedRoute,private routerObj:Router){}


name:any
price:any
company:any
ngOnInit(){
  this.actRouteObj.paramMap.subscribe((param)=>{
    this.id=param.get('id')
    this.dbServ.getRecordById("product",this.id).subscribe((res)=>{
      this.prodData=res
      this.name=this.prodData.pname
      this.price=this.prodData.price
      this.company=this.prodData.company
      
    })



    this.prodDataUpdate = new FormGroup({
      pname:new FormControl(this.name,[Validators.required,Validators.pattern('^[a-zA-Z]{3,20}$')]),
      price:new FormControl(this.price,[Validators.required,Validators.pattern('^[0-9]{3,20}$')]),
      company:new FormControl(this.company,[Validators.required,Validators.pattern('^[a-zA-Z]{3,20}$')])
    }
    )
  })


 
}


addData(){
  console.log(this.prodData.value)
  this.dbServ.addRecord("product",this.prodData.value).subscribe(()=>{

    window.alert("Record Added successfully")
    this.routerObj.navigate(['/maindashboard/products'])
  })
}
}
