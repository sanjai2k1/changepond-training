import { Component } from '@angular/core';
import { DatabaseServiceService } from '../../shared/service/database-service.service';

@Component({
  selector: 'app-product-dashboard',
  templateUrl: './product-dashboard.component.html',
  styleUrl: './product-dashboard.component.css'
})
export class ProductDashboardComponent {
myproducts:any
constructor(private dbserv:DatabaseServiceService){
  
}


ngOnInit(){
  this.myproducts = this.dbserv.getRecord("product").subscribe((res)=>{
    this.myproducts=res
    console.log(res)
  })
}

}
