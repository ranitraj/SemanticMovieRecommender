import os
import pymongo
import requests

import urls

from dotenv import load_dotenv

# Load dotEnv
load_dotenv()

# Load Local environment variables
mongo_atlas_uri = os.getenv('URI_MOVIE_RECOMMENDER')
mongo_atlas_password = os.getenv('PASSWORD_MOVIE_RECOMMENDER')
hugging_face_api_token = os.getenv('HUGGING_FACE_TOKEN')

# Replace password in uri-template with the password env variable
movie_recommender_uri = mongo_atlas_uri.replace('<password>', mongo_atlas_password)

# Part-1: Initialize PyMongo Client & database
client = pymongo.MongoClient(movie_recommender_uri)
movie_database = client.sample_mflix

# Get 'movies' collection from movie_database
movies_collection = movie_database.movies


# Part-2: Get Vector-Embedding from a Sentence using HuggingFace sentence-transformers 'all-MiniLM-L6-v2' model via AP
def get_vector_embeddings(payload: str) -> list[float]:
    print(f"Generating Vector Embeddings for text == ${payload}")

    api_response = requests.post(
        urls.API_GENERATE_EMBEDDINGS,
        headers={"Authorization": f"Bearer {hugging_face_api_token}"},
        json={"inputs": payload}
    )

    if api_response.status_code != 200:
        raise ValueError(f"Request failed with Status-Code: {api_response.status_code} & Message: {api_response.text}")

    return api_response.json()


# Print Embeddings
print(get_vector_embeddings("Hello World!"))

