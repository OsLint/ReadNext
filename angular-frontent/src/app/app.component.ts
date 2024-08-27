import {Component} from '@angular/core';
import {Router, RouterOutlet} from '@angular/router';
import {NgIf, NgOptimizedImage} from "@angular/common";
import {NavbarComponent} from "./components/navbar/navbar.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NgOptimizedImage, NavbarComponent, NgIf],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'ReadNext';

  constructor(private router: Router) {}

  isAuthPage(): boolean {
    return this.router.url.includes('login') || this.router.url.includes('register');
  }
}
