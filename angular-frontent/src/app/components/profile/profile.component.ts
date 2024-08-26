import { Component } from '@angular/core';
import {NavbarComponent} from "../navbar/navbar.component";

@Component({
  selector: 'app-profile',
  standalone: true,
    imports: [
        NavbarComponent
    ],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.scss'
})
export class ProfileComponent {

}
