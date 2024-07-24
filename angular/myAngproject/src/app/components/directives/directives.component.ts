import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';



@Component({
  selector: 'app-directives',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './directives.component.html',
  styleUrl: './directives.component.css'
})

export class DirectivesComponent {
  isCondition: boolean = false;
  hasValue: boolean = true;
  selectedcourse:string = "";
  frontend : string[] = ['Html','css','Bootstrap','Sass','Javascript','React','Angular'];
  employee:any[] = [
    {id:101,name:"Vijay",post:"Manager",company:"Changepond"},
    {id:102,name:"Ajith",post:"Manager",company:"Microsoft"},
    {id:103,name:"Suresh",post:"Manager",company:"Tesla"},
    {id:104,name:"Hamsavan",post:"Manager",company:"Google"},

  ];
  selectedCourse : string = "Sass";
  courses:any[] =['HTML','CSS','Bootstrap','Sass','Javascript','React','Angular'];
  greeting(event:Event){
    const target = event.target as HTMLElement;
    this.selectedcourse =target.innerHTML;
  }
}
