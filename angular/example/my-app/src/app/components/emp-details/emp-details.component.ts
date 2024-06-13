import { Component } from '@angular/core';

@Component({
  selector: 'app-emp-details',
  templateUrl: './emp-details.component.html',
  styleUrl: './emp-details.component.css'
})
export class EmpDetailsComponent {


  emp:any =[
    {id:101,name:"Ajit",salary:95000,post:"Manager",address:"chennai"},
    {id:102,name:"Vijay",salary:30000,post:"Manager",address:"Tiruvallur"},
    {id:103,name:"Suresh",salary:60000,post:"Manager",address:"chengalpattu"},
    {id:104,name:"Danish",salary:97000,post:"Manager",address:"Vellore"},
    {id:105,name:"Raja",salary:28000,post:"Manager",address:"Trichy"},
    {id:105,name:"Raja",salary:28000,post:"Manager",address:"Pune"}
  ]
}
