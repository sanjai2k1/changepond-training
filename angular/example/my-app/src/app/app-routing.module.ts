import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DatabindingComponent } from './components/databinding/databinding.component';
import { DirectiveComponent } from './components/directive/directive.component';
import { ToggleImgComponent } from './Task/toggle-img/toggle-img.component';
import { ToggleListComponent } from './Task/toggle-list/toggle-list.component';
import { PagenotfoundComponent } from './components/pagenotfound/pagenotfound.component';
import { EmpDetailsComponent } from './components/emp-details/emp-details.component';
import { AngFormComponent } from './components/ang-form/ang-form.component';
import { MainDashboardComponent } from './components/main-dashboard/main-dashboard.component';
import { RtfComponent } from './components/rtf/rtf.component';
import { BreakfastComponent } from './components/breakfast/breakfast.component';
import { ProductDashboardComponent } from './crud/product-dashboard/product-dashboard.component';
import { ProductAddComponent } from './crud/product-add/product-add.component';
import { ProducUpdateComponent } from './crud/produc-update/produc-update.component';

const routes: Routes = [
  // 2.default routing 
  // {path:"",component:DatabindingComponent},

  //3. redirect routing
  // {path:"",redirectTo:"databinding",pathMatch:"full"},

  {path:"maindashboard",component:MainDashboardComponent,children:[

 //1.naming routing
 {path:"databinding",component:DatabindingComponent},
 {path:"directives",component:DirectiveComponent},
 {path:"toggleimg",component:ToggleImgComponent},
 {path:"togglelist",component:ToggleListComponent},
 {path:"breakfast",component:BreakfastComponent},
 {path:"productadd",component:ProductAddComponent},
 {path:"productupdate/:id",component:ProducUpdateComponent},

 {path:"products",component:ProductDashboardComponent},


 //4. parameterize routing
 {path:"empdetail/:id",component:EmpDetailsComponent},
 {path:"empdetail",component:EmpDetailsComponent},

 //5. child routing
 {path:"angform",component:AngFormComponent,children:[
  {
    path:"",component:RtfComponent
  }, 
  {
     path:"rtf",component:RtfComponent
   }
 ]},
 {path:"empdetail",component:EmpDetailsComponent},

  ]},


 


  //6.wildcard routing
  {path:"**",component:PagenotfoundComponent}


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
