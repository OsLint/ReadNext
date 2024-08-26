import {RouterModule, Routes} from '@angular/router';
import {NgModule} from "@angular/core";
import {HomeComponent} from "./home/home.component";

export const routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'home', component: HomeComponent},
  {path: 'about', component: AboutComponent},
  {path: 'contact', component: ContactComponent},
];
