import { Component } from '@angular/core';
import { sample } from 'rxjs';

@Component({
  selector: 'app-mypipe',
  templateUrl: './mypipe.component.html',
  styleUrl: './mypipe.component.css'
})
export class MypipeComponent {
msg:string = "Hello friend,you all are fantastic participant."

emp:any={
  id:101,
  name:"Ajit",
  salary:85000
}
}
