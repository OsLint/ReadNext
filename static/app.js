function handleImageError(image) {
    image.onerror = null;
    image.src = '/static/placeholder.jpg';
}

function toggleLike(bookId, isLiked) {
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
            likeButton.textContent = `${data.isLiked ? 'Liked' : 'Like'} (${data.likes})`;
            likeButton.style.backgroundColor = data.isLiked ? 'darkslategray' : 'teal';
            likeButton.setAttribute('onclick', `toggleLike(${bookId}, ${data.isLiked})`);
        } else {
            alert(data.message || 'Error toggling like status.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

