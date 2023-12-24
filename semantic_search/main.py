import os

from dotenv import load_dotenv

from database.movie_database import MovieDatabase
from database.mongo_atlas_client import MongoAtlasClient
from api.hugging_face_api import HuggingFaceAPI
from api.vector_embedding_service import VectorEmbeddingService


# Load environment variables
load_dotenv()
mongo_atlas_uri = os.getenv('URI_MOVIE_RECOMMENDER')
mongo_atlas_password = os.getenv('PASSWORD_MOVIE_RECOMMENDER')
hugging_face_api_token = os.getenv('HUGGING_FACE_TOKEN')

# Initialize clients
db_client = MongoAtlasClient(mongo_atlas_uri, mongo_atlas_password)
api_client = HuggingFaceAPI(hugging_face_api_token)

# Initialize Database
movie_db = MovieDatabase(db_client)

# Initialize API Services
embedding_service = VectorEmbeddingService(api_client)


# Get all movies
movies_collection = movie_db.get_all_movies()

# Inserts vector-embedding columns (if they don't already exist)
movie_db.insert_movie_plot_embedding_column(
    movies_collection=movies_collection,
    embedding_service=embedding_service
)

movie_db.insert_movie_title_embedding_column(
    movies_collection=movies_collection,
    embedding_service=embedding_service
)

# Sample query
query = "man plotting a crime against society"

# Get Top-3 recommendations based on Plot
recommendations = movie_db.get_plot_recommendations(
    query=query,
    movies_collection=movies_collection,
    embedding_service=embedding_service
)

# Print the movie Name & Plot for the recommended movies
for cur_recommendation in recommendations:
    print(f'Movie Name: {cur_recommendation["title"]},\nMovie Plot: {cur_recommendation["plot"]}\n')
