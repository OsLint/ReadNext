# 📚 ReadNext

## Disclaimer
This project was originally  developed for my PPY (Programming in Python) class at the Polish Japanese Academy of Information Technology
You can see the state it was in when you go back to commits from the june 2024.

## Overview

The Book Recommendations System is a web application that helps users discover books tailored to their interests. Users can explore a diverse collection of books, view recommendations, and manage their profiles.

### Explore Page
<img src="https://github.com/okdotdev/book-recomendation-api-knn-python-flask/assets/106467480/850afa65-4de9-45ea-a13d-dbd18ec8b2a5" alt="Explore" width="400"/>

### Profile Page
<img src="https://github.com/okdotdev/book-recomendation-api-knn-python-flask/assets/106467480/f2b99afe-2752-4889-90f5-4b7078ea1a70" alt="Profile" width="400"/>

### Recommendations Page
<img src="https://github.com/okdotdev/book-recomendation-api-knn-python-flask/assets/106467480/35554e37-1655-4adb-89fc-3ae606fdc928" alt="Recommendations" width="400"/>


## Features

- 🔍 **Book Search:** Search for books by title, author, year, or genre.
- 👤 **User Profiles:** View and manage your liked books.
- 🎯 **Personalized Recommendations:** Receive book recommendations based on your likes and preferences.

## Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Flask
- Flask-Migrate

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```bash
    flask db init
    flask db migrate -m "initial migration"
    flask db upgrade
    ```

5. Seed the database with initial data (if needed):
    ```bash
    flask seed_db
    ```

### Running the App

Start the Flask development server:
```bash
flask run
```
Open your browser and navigate to http://127.0.0.1:5000 to access the app.


## 🚫Common errors

If you encounter a 403 error when trying to log in or run the app using Chrome or Chromium, try clearing the socket pool:
Open a new tab and go to:
```
chrome://net-internals/#sockets
```
Click on "Flush socket pools."

