import { Component } from '@angular/core';
import {NavbarComponent} from "../navbar/navbar.component";
import {BookGridComponent} from "../book-grid/book-grid.component";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    NavbarComponent,
    BookGridComponent
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {

}
