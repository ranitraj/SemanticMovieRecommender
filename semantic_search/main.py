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

# Example usage
sentence = "Hello World!"
embeddings = embedding_service.get_vector_embeddings(sentence)
print(embeddings)
