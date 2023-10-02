from storage_json import StorageJson
from movie_app import MovieApp
from storage_csv import StorageCsv

storage = StorageCsv('movies.csv')
movie_app = MovieApp(storage)
movie_app.run()


def main():
    # Create a StorageJson object
    storage = StorageJson('movies.json')

    # Create a MovieApp object with the StorageJson object
    app = MovieApp(storage)

    # Run the app
    app.run()


# Check if this file is being run as the main module
if __name__ == "__main__":
    main()