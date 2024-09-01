import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {catchError, Observable, throwError} from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class BookService {
  private baseUrl = 'http://127.0.0.1:5000/api';

  constructor(private http: HttpClient) {
  }


 // getBooks(page: number): Observable<any> {
 //   const url = `${this.baseUrl}/books?page=${page}`;
 //   return this.http.get<any>(url).pipe(catchError(this.handleError));
 // }

  getBooks(page: number): Observable<any> {
    const url = `${this.baseUrl}/books`;
    return this.http.get<any>(url).pipe(catchError(this.handleError));
  }

  toggleLike(bookId: number, liked: boolean): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/books/${bookId}/like`, {liked});
  }

  private handleError(error: HttpErrorResponse): Observable<never> {
    let errorMessage = 'An unknown error occurred!';
    if (error.error instanceof ErrorEvent) {
      errorMessage = `Client-side error: ${error.error.message}`;
    } else {
      errorMessage = `Server-side error: ${error.status} - ${error.message}`;
    }
    console.error(errorMessage);
    return throwError(() => new Error(errorMessage));
  }
}
