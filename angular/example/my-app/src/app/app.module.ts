import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DatabindingComponent } from './components/databinding/databinding.component';
import { DirectiveComponent } from './components/directive/directive.component';
import {FormsModule} from '@angular/forms';
import { ToggleImgComponent } from './Task/toggle-img/toggle-img.component';
import { ToggleListComponent } from './Task/toggle-list/toggle-list.component';
import { MypipeComponent } from './components/mypipe/mypipe.component'

@NgModule({
  declarations: [
    AppComponent,
    DatabindingComponent,
    DirectiveComponent,
    ToggleImgComponent,
    ToggleListComponent,
    MypipeComponent
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
