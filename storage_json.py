from istorage import IStorage
import os
import json


class StorageJson(IStorage):
       def __init__(self, file_path):
        self.file_path = file_path

       def list_movies(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                file.write('{}')
        with open(self.file_path, 'r') as file:
            return json.load(file)

       def add_movie(self, title, year, rating, poster):
        with open(self.file_path, 'r') as file:
          data = json.load(file)

        data[title] = {
            "year": year,
            "rating": rating,
            "poster": poster
        }

        with open(self.file_path, 'w') as file:
            json.dump(data, file)

       def delete_movie(self, title):
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        if title in data:
            del data[title]

        with open(self.file_path, 'w') as file:
            json.dump(data, file)

       def update_movie(self, title, rating):
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        if title in data:
            data[title]['rating'] = rating

        with open(self.file_path, 'w') as file:
            json.dump(data, file)