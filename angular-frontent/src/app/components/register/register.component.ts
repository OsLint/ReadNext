import { Component , ViewEncapsulation } from '@angular/core';
import {NgIf, NgOptimizedImage} from "@angular/common";
import {Router, RouterLink, RouterModule} from "@angular/router";
import {HttpClient, HttpClientModule} from "@angular/common/http";
import {FormsModule} from "@angular/forms";
import {catchError, of, tap} from "rxjs";

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [
    NgOptimizedImage,
    RouterLink,
    HttpClientModule,
    RouterModule,
    FormsModule,
    NgIf
  ],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss',
  encapsulation: ViewEncapsulation.None
})
export class RegisterComponent {
  email: string = '';
  userName: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private http: HttpClient, private router: Router) {
  }

  onSubmit() {
    this.errorMessage = '';

    this.http.post('/api/register', {userName: this.userName, password: this.password}).pipe(
      tap((response: any) => {
        if (response.status === 'success') {
          this.router.navigate(['/home']).then();
        } else {
          this.errorMessage = 'Register failed. User already exists.';
        }
      }),
      catchError((error) => {
        console.log(error)
        this.errorMessage = 'An error occurred. Please try again.';
        return of(null);
      })
    ).subscribe();
  }
}
