import {RouterModule, Routes} from '@angular/router';
import {NgModule} from "@angular/core";
import {HomeComponent} from "./components/home/home.component";
import {RecomendationsComponent} from "./components/recomendations/recomendations.component";
import {LoginComponent} from "./components/login/login.component";
import {ProfileComponent} from "./components/profile/profile.component";
import {RegisterComponent} from "./components/register/register.component";
import {BookGridComponent} from "./components/book-grid/book-grid.component";

export const routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'home', component: HomeComponent},
  {path: 'recommendations', component: RecomendationsComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'login', component: LoginComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'book-grid', component: BookGridComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
