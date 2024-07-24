import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { DatabindingComponent } from './components/databinding/databinding.component';
import { DirectivesComponent } from './components/directives/directives.component';
import { MychoiceComponent } from './task/mychoice/mychoice.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,DatabindingComponent,DirectivesComponent,MychoiceComponent  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'myAngproject';
}
