import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DatabindingComponent } from './components/databinding/databinding.component';
import { DirectiveComponent } from './components/directive/directive.component';
import {FormsModule,ReactiveFormsModule} from '@angular/forms';
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
import { FooterComponent } from './components/footer/footer.component';
import { BreakfastComponent } from './components/breakfast/breakfast.component';
import { ProductDashboardComponent } from './crud/product-dashboard/product-dashboard.component';
import { ProductAddComponent } from './crud/product-add/product-add.component';
import { ProducUpdateComponent } from './crud/produc-update/produc-update.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { AngualarmaterialComponent } from './components/angualarmaterial/angualarmaterial.component'
import {MatButtonModule} from "@angular/material/button";
import { LoginComponent } from './components/login/login.component'


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
    FooterComponent,
    BreakfastComponent,
    ProductDashboardComponent,
    ProductAddComponent,
    ProducUpdateComponent,
    AngualarmaterialComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    MatButtonModule
  ],
  
  providers: [
    provideClientHydration(),
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
