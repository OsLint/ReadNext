import { Component } from '@angular/core';
import {NgIf, NgOptimizedImage} from "@angular/common";
import {RouterLink} from "@angular/router";
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [
    NgOptimizedImage,
    RouterLink,
    NgIf
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent {
  

}
