from .mongo_atlas_client import MongoAtlasClient


class MovieDatabase:
    def __init__(self, db_client: MongoAtlasClient):
        self.movie_database = db_client.client.sample_mflix

    def get_all_movies(self):
        """
        Retrieves the entire movies collection from the database and prints the total number of movies.
        This method accesses the 'movies' collection in the movie database, counts the total number of movie documents,
        prints this count, and then returns the collection for further use or processing.

        Returns:
            A MongoDB collection object representing all the movies in the database.
        """
        movies_collection = self.movie_database.movies
        print(f"Number of Movies in Database = {movies_collection.count_documents({})}")
        return movies_collection

    @staticmethod
    def insert_movie_title_embedding_column(movies_collection, embedding_service):
        """
        Updates the movies collection by adding a 'movie_title_embedding' field for each movie with a title.
        This method iterates through all movies that have a 'title' field, computes their title embeddings
        using the provided embedding service, and updates each movie document with the new 'movie_title_embedding'
        field only if it doesn't already exist.

        The purpose of adding an embedding for the movie titles is typically to facilitate similarity searches,
        recommendations, or other machine learning tasks where a numerical representation of text is useful.

        Parameters:
        movies_collection: A MongoDB collection object representing the movies.
        embedding_service: An object or service capable of providing vector embeddings for text.

        Note: This operation replaces the entire document for each movie with its updated version
              only if the 'movie_title_embedding' field is not already present.
        """
        for cur_movie in movies_collection.find({'title': {"$exists": True}}):
            # Check if 'movie_title_embedding' already exists
            if 'movie_title_embedding' not in cur_movie:
                # Compute the embedding vector for the current movie's title
                cur_movie['movie_title_embedding'] = embedding_service.get_vector_embeddings(cur_movie['title'])
                # Replace the old movie document with the updated one (now including title embeddings)
                movies_collection.replace_one({'_id': cur_movie['_id']}, cur_movie)

    @staticmethod
    def insert_movie_plot_embedding_column(movies_collection, embedding_service):
        """
        Updates the movies collection by adding a 'movie_plot_embedding' field for each movie.
        This method iterates through the list of movies in the given collection that have a 'plot' field,
        computes their plot embeddings using the provided embedding service, and then updates each movie
        document with the new 'movie_plot_embedding' field only if it doesn't already exist.

        Parameters:
        movies_collection: A MongoDB collection object representing the movies.
        embedding_service: An object capable of providing vector embeddings for text

        Note: This operation replaces the entire document for each movie with its updated version
              only if the 'movie_plot_embedding' field is not already present.
        """
        for cur_movie in movies_collection.find({'plot': {"$exists": True}}):
            # Check if 'movie_plot_embedding' already exists
            if 'movie_plot_embedding' not in cur_movie:
                # Compute the embedding vector for the current movie's plot
                cur_movie['movie_plot_embedding'] = embedding_service.get_vector_embeddings(cur_movie['plot'])
                # Replace the old movie document with the updated one (now including plot embeddings)
                movies_collection.replace_one({'_id': cur_movie['_id']}, cur_movie)

    @staticmethod
    def get_plot_recommendations(query, movies_collection, embedding_service):
        recommendations = movies_collection.aggregate([
            {

            }
        ])
