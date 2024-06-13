import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DatabindingComponent } from './components/databinding/databinding.component';
import { DirectiveComponent } from './components/directive/directive.component';
import {FormsModule} from '@angular/forms';
import { ToggleImgComponent } from './Task/toggle-img/toggle-img.component';
import { ToggleListComponent } from './Task/toggle-list/toggle-list.component';
import { MypipeComponent } from './components/mypipe/mypipe.component';
import { CubePipe } from './shared/Custompipe/cube.pipe';
import { AreaOfSquarePipe } from './shared/Custompipe/area-of-square.pipe';
import { AreaOfCirclePipe } from './shared/Custompipe/area-of-circle.pipe';
import { EmpDetailsComponent } from './components/emp-details/emp-details.component'

@NgModule({
  declarations: [
    AppComponent,
    DatabindingComponent,
    DirectiveComponent,
    ToggleImgComponent,
    ToggleListComponent,
    MypipeComponent,
    CubePipe,
    AreaOfSquarePipe,
    AreaOfCirclePipe,
    EmpDetailsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
