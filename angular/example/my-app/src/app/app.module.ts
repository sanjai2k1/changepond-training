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
import { EmpDetailsComponent } from './components/emp-details/emp-details.component';
import { AngFormComponent } from './components/ang-form/ang-form.component';
import { PagenotfoundComponent } from './components/pagenotfound/pagenotfound.component';
import { MainDashboardComponent } from './components/main-dashboard/main-dashboard.component';
import { RtfComponent } from './components/rtf/rtf.component';
import { UtdfComponent } from './components/utdf/utdf.component';
import { NavComponent } from './components/nav/nav.component';
import { FooterComponent } from './components/footer/footer.component'

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
    EmpDetailsComponent,
    AngFormComponent,
    PagenotfoundComponent,
    MainDashboardComponent,
    RtfComponent,
    UtdfComponent,
    NavComponent,
    FooterComponent
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
