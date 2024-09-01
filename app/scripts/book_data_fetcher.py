import requests
import json

API_KEY = ''
QUERY = 'fiction'
MAX_RESULTS = 40
NUM_REQUESTS = 25

books = []

for i in range(NUM_REQUESTS):
    response = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q={QUERY}&startIndex={i * MAX_RESULTS}&maxResults={MAX_RESULTS}&key={API_KEY}')
    if response.status_code == 200:
        data = response.json()
        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            publication_date = volume_info.get('publishedDate', 'N/A')
            if publication_date != 'N/A' and len(publication_date) >= 4:
                publication_year = publication_date[:4]
            else:
                publication_year = 'N/A'

            book = {
                "title": volume_info.get('title', 'N/A'),
                "author": ', '.join(volume_info.get('authors', ['N/A'])),
                "short_description": volume_info.get('description', 'N/A'),
                "genre": ', '.join(volume_info.get('categories', ['N/A'])),
                "cover_photo_url": volume_info.get('imageLinks', {}).get('thumbnail', 'N/A'),
                "publication_year": publication_year
            }
            books.append(book)
    else:
        print(f"Failed to fetch data: {response.status_code}")
    if len(books) >= 1000:
        break

with open('./instance/books.json', 'w') as f:
    json.dump(books[:1000], f, indent=4)

print("Generated books.json with 1000 books.")
