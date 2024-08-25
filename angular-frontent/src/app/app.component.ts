import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {NgOptimizedImage} from "@angular/common";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NgOptimizedImage],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'angular-frontent';


   handleImageError(image: HTMLImageElement) {
    image.onerror = null;
    image.src = '/static/placeholder.jpg';
}

 toggleLike(bookId: number, isLiked: boolean) {
    const url = isLiked ? '/dislike_book' : '/like_book';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ book_id: bookId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.likes !== undefined) {
            const likeButton = document.querySelector(`.book-card[data-book-id="${bookId}"] .like-button`);
            // @ts-ignore
          likeButton.textContent = `${data.isLiked ? 'Liked' : 'Like'} (${data.likes})`;
            // @ts-ignore
          likeButton.style.backgroundColor = data.isLiked ? 'darkslategray' : 'teal';
            // @ts-ignore
          likeButton.setAttribute('onclick', `toggleLike(${bookId}, ${data.isLiked})`);
        } else {
            alert(data.message || 'Error toggling like status.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


}
