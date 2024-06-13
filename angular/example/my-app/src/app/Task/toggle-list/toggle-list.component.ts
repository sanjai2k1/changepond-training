import { Component } from '@angular/core';

@Component({
  selector: 'app-toggle-list',
  templateUrl: './toggle-list.component.html',
  styleUrl: './toggle-list.component.css'
})
export class ToggleListComponent {
  bikes:string[]=['HeroHond','BMW','Yahama','JavaBike','Bajaj']
  cars:string[]=['Suzuki Swift','Hyundai','Mahindra','kia','Renault']
}
