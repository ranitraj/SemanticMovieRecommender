from .mongo_atlas_client import MongoAtlasClient


class MovieDatabase:
    def __init__(self, db_client: MongoAtlasClient):
        self.movie_database = db_client.client.sample_mflix

    def get_all_movies(self):
        movies_collection = self.movie_database.movies
        print(f"Number of Movies in Database = {movies_collection.count_documents({})}")
        return movies_collection

