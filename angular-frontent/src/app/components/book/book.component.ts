import {Component, Input, Output, EventEmitter} from '@angular/core';
import {Book} from "../../interfaces/book";
import {NgIf, NgOptimizedImage, NgStyle, SlicePipe} from "@angular/common";

@Component({
  selector: 'app-book',
  standalone: true,
  imports: [
    NgOptimizedImage,
    SlicePipe,
    NgStyle,
    NgIf
  ],
  templateUrl: './book.component.html',
  styleUrl: './book.component.scss'
})
export class BookComponent {
  @Input() book: Book | undefined;
  @Output() likeToggled = new EventEmitter<number>();

  handleImageError(event: Event): void {
    const target = event.target as HTMLImageElement;
    target.src = '/assets/placeholder.jpg';
  }

  toggleLike(): void {
    // @ts-ignore
    this.likeToggled.emit(this.book.id);
  }
}
