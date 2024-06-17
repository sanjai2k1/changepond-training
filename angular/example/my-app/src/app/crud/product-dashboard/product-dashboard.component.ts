import { Component } from '@angular/core';
import { DatabaseServiceService } from '../../shared/service/database-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-product-dashboard',
  templateUrl: './product-dashboard.component.html',
  styleUrl: './product-dashboard.component.css'
})
export class ProductDashboardComponent {
myproducts:any
some:any
constructor(private dbserv:DatabaseServiceService,private routerObj:Router){
  
}



ngOnInit(){
this.fetchData()
}

fetchData(){
  this.dbserv.getRecord("product").subscribe((res)=>{
    this.myproducts=res
   
  })
}
delete(id:any){
  if(window.confirm(`delete ${id}`)){
    this.dbserv.deleteRecord("product",id).subscribe(()=>{
      window.alert("deleted")
      this.fetchData()
    })

  }
}

}
