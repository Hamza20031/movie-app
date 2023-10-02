class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        for title, details in movies.items():
            print(f"Title: {title}")
            print(f"Year: {details['year']}")
            print(f"Rating: {details['rating']}")
            print("-----------")

    def _command_add_movie(self):
        title = input("Enter movie title: ")
        year = int(input("Enter movie year: "))
        rating = float(input("Enter movie rating: "))
        poster = input("Enter movie poster path: ")

        self._storage.add_movie(title, year, rating, poster)
        print(f"{title} added successfully!")

    def _command_movie_stats(self):
        movies = self._storage.list_movies()
        # For demonstration, let's show the total number of movies
        print(f"Total number of movies: {len(movies)}")

    def _command_delete_movie(self):
        title = input("Enter the title of the movie to delete: ")
        self._storage.delete_movie(title)
        print(f"{title} deleted successfully!")

    def _command_update_movie(self):
        title = input("Enter the title of the movie to update: ")
        rating = float(input(f"Enter new rating for {title}: "))
        self._storage.update_movie(title, rating)
        print(f"{title} updated successfully!")

    def _generate_website(self):
        # Placeholder for future implementation to generate a website
        pass

    def run(self):
        while True:
            print("\nMenu:")
            print("1. List Movies")
            print("2. Add Movie")
            print("3. Delete Movie")
            print("4. Update Movie Rating")
            print("5. Show Movie Stats")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "4":
                self._command_update_movie()
            elif choice == "5":
                self._command_movie_stats()
            elif choice == "6":
                print("Exiting Movie App!")
                break
            else:
                print("Invalid choice! Try again.")


if __name__ == "__main__":
    from storage_json import StorageJson

    storage = StorageJson("movies.json")
    app = MovieApp(storage)
    app.run()

