import os
import pymongo

from dotenv import load_dotenv

# Load dotEnv
load_dotenv()

# Load Local environment variables
mongo_atlas_uri = os.getenv('URI_MOVIE_RECOMMENDER')
mongo_atlas_password = os.getenv('PASSWORD_MOVIE_RECOMMENDER')

# Replace password in uri-template with the password env variable
movie_recommender_uri = mongo_atlas_uri.replace('<password>', mongo_atlas_password)

# Initialize PyMongo Client & Database
client = pymongo.MongoClient(movie_recommender_uri)
movie_database = client.sample_mflix

# Test Connection & Print results
movies_collection = movie_database.movies.find().limit(2)
for cur_movie in movies_collection:
    print(cur_movie)

