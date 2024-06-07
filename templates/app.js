async function addUser() {
    const username = document.getElementById('username').value;
    const response = await fetch('/add_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username}),
    });
    const result = await response.json();
    alert(result.message);
}

async function addBook() {
    const title = document.getElementById('book').value;
    const response = await fetch('/add_book', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({title}),
    });
    const result = await response.json();
    alert(result.message);
}

async function addPreference() {
    const user_id = document.getElementById('user-id').value;
    const book_id = document.getElementById('book-id').value;
    const rating = document.getElementById('rating').value;
    const response = await fetch('/add_preference', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({user_id, book_id, rating}),
    });
    const result = await response.json();
    alert(result.message);
}

async function getRecommendations() {
    const user_id = document.getElementById('user-id').value;
    const response = await fetch(`/recommend/${user_id}`);
    const recommendations = await response.json();
    const recommendationsDiv = document.getElementById('recommendations');
    recommendationsDiv.innerHTML = '<h3>Recommendations:</h3>';
    recommendations.forEach(book => {
        const p = document.createElement('p');
        p.textContent = book;
        recommendationsDiv.appendChild(p);
    });
}


console.log('app.js loaded')