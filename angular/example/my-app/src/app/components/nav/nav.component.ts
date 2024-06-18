import { Component } from '@angular/core';
import { DatabaseServiceService } from '../../shared/service/database-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.css'
})
export class NavComponent {

  constructor(private routerObj : Router){

  }


  signOut(){
    sessionStorage.clear()
    this.routerObj.navigate([''])

  }
}
