from .mongo_atlas_client import MongoAtlasClient


class MovieDatabase:
    def __init__(self, db_client: MongoAtlasClient):
        self.movie_database = db_client.client.sample_mflix
        self.movies_collection = self.movie_database.movies
