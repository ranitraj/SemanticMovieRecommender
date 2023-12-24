# Movie Recommender Based on Semantic Search

## Overview
This movie recommender uses semantic search to suggest movies based on user's mood or query, leveraging MongoDB's Atlas Search for vector similarity matching refering https://www.youtube.com/watch?v=JEBDfGqrAUA.

## Features
- **Semantic Search**: Utilizes embeddings to understand the query contextually.
- **Atlas Search Integration**: Leverages MongoDB's Atlas Search for efficient vector matching.
- **Customizable Recommendations**: Easily adaptable to different moods or genres.

## Setup

### Install Dependencies
Install all necessary dependencies by running:
```bash
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add all necessary API keys and Database URIs like so:
```bash
API_KEY=your_api_key_here
DB_URI=your_mongodb_uri_here
```


### Atlas Vector Search Setup
1. Go to the 'Atlas Search' tab in your MongoDB Atlas dashboard.
2. Create a new search index as JSON:
```json
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "movie_plot_embedding": {
        "dimensions": 384,
        "similarity": "dotProduct",
        "type": "knnVector"
      }
    }
  }
}
```

## Usage
Run get_plot_recommendations(query, movies_collection, embedding_service) to get movie recommendations based on the provided query.

