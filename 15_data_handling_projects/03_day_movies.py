import json
import os

FILENAME = "movies.json"


def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", encoding="utf8") as f:
            json.dump([], f, indent=2)
        print("Created 'movies.json' with an empty list.")

def load_movies():
    try:
        with open(FILENAME, mode="r", encoding="utf8") as f:
            # print(json.load(f))
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_movies(movies):
    with open(FILENAME, mode="w", encoding="utf8") as f:
        json.dump(movies, f, indent=2)


def add_movie():
    movies = load_movies()
    title = input("Enter movie title: ").strip()
    genre = input("Enter genre: ").strip()

    try:
        rating = float(input("Enter rating (0-10): ").strip())
        if not (0 <= rating <= 10):
            raise ValueError("Rating must be between 0 and 10.")
    except ValueError as e:
        print("Invalid rating:", e)
        return

    # Duplicate check
    for movie in movies:
        if movie["title"].lower() == title.lower():
            print("Movie already exists.")
            return

    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    movies.append(new_movie)
    save_movies(movies)
    print(" Movie added successfully.")


def view_movies():
    movies = load_movies()
    if not movies:
        print("No movies found.")
        return

    print("\n🎬 All Movies:")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['title']} | Genre: {movie['genre']} | Rating: {movie['rating']}")

def search_movies():
    movies = load_movies()
    if not movies:
        print("No movies to search.")
        return

    keyword = input("Enter keyword to search (title or genre): ").lower()
    matches = [m for m in movies if keyword in m["title"].lower() or keyword in m["genre"].lower()]

    if matches:
        print("\n🔍 Search Results:")
        for i, movie in enumerate(matches, 1):
            print(f"{i}. {movie['title']} | Genre: {movie['genre']} | Rating: {movie['rating']}")
    else:
        print("No matching movies found.")


def main():
    initialize_file()

    while True:
        print("\n📽️  Personal Movie Tracker")
        print("1. Add movie")
        print("2. View all movies")
        print("3. Search movies")
        print("4. Exit\n")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        match choice:
            case 1:
                add_movie()
            case 2:
                view_movies()
            case 3:
                search_movies()
            case 4:
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
