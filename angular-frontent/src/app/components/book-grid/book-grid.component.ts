import {Component} from '@angular/core';
import {BookService} from "../../services/book/book.service";
import {RouterLink} from "@angular/router";
import {NgForOf, NgIf} from "@angular/common";
import {BookComponent} from "../book/book.component";
import {HttpClientModule} from "@angular/common/http";
import {Book} from "../../interfaces/book";

@Component({
  selector: 'app-book-grid',
  standalone: true,
  imports: [
    HttpClientModule,
    RouterLink,
    NgIf,
    BookComponent,
    NgForOf
  ],
  templateUrl: './book-grid.component.html',
  styleUrl: './book-grid.component.scss',
})
export class BookGridComponent {
  books: Book[] = [];
  page: number = 1;

  constructor(private bookService: BookService) {
  }

  ngOnInit(): void {
    console.log('ngOnInit called in BookGridComponent');
    this.loadBooks();
  }

  loadBooks(): void {
    this.bookService.getBooks(this.page).subscribe(data => {
      console.log('Data received:', data);
      this.books = data.books;
      this.page = data.page;
    });
  }

  onLikeToggled(bookId: number): void {
    this.bookService.toggleLike(bookId, true).subscribe(() => {
      this.loadBooks();
    });
  }
}
