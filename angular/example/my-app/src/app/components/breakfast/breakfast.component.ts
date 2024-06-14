import { Component } from '@angular/core';
import { MyServiceService } from '../../shared/service/my-service.service';

@Component({
  selector: 'app-breakfast',
  templateUrl: './breakfast.component.html',
  styleUrl: './breakfast.component.css'
})
export class BreakfastComponent {
  items:any
  constructor(private myserObj:MyServiceService){

    
  }


  ngOnInit(){
    this.items = this.myserObj.breakfast
  }
}
