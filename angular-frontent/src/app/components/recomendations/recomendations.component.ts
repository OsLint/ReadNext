import { Component } from '@angular/core';
import {NavbarComponent} from "../navbar/navbar.component";

@Component({
  selector: 'app-recomendations',
  standalone: true,
    imports: [
        NavbarComponent
    ],
  templateUrl: './recomendations.component.html',
  styleUrl: './recomendations.component.scss'
})
export class RecomendationsComponent {

}
