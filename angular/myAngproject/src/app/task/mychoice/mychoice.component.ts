import { Component } from '@angular/core';

@Component({
  selector: 'app-mychoice',
  standalone: true,
  imports: [],
  templateUrl: './mychoice.component.html',
  styleUrl: './mychoice.component.css'
})
export class MychoiceComponent {
  samosa: boolean = false;
  dosa: boolean = false;
  idli: boolean = false;
  ans: string = "";
  
  samosaeve() {
  this.samosa = this.samosa ? false : true;
  this.updateAns();
  console.log(this.ans);
  this.alert();
  }
  
  dosaeve() {
  this.dosa = this.dosa ? false : true;
  this.updateAns();
  console.log(this.ans);
  this.alert();
  }
  
  idlieve() {
  this.idli = this.idli ? false : true;
  this.updateAns();
  console.log(this.ans);
  this.alert();
  }
  
  updateAns() {
  this.ans = (this.samosa ? "samosa " : "") + 
  (this.dosa ? "dosa " : "") + 
  (this.idli ? "idli" : "");
  }
  
  alert() {
  window.alert(this.ans);
  }
}
