import requests
from .hugging_face_api import HuggingFaceAPI

from .urls import API_GENERATE_EMBEDDINGS as API_URL


# Generates Embeddings using https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 via Inference API
class VectorEmbeddingService:
    def __init__(self, api_client: HuggingFaceAPI):
        self.api_client = api_client

    def get_vector_embeddings(self, payload: str) -> list[float]:
        print(f"Generating Vector Embeddings for text: {payload}")
        api_response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {self.api_client.api_token}"},
            json={"inputs": payload}
        )
        if api_response.status_code != 200:
            raise ValueError(
                f"Request failed with Status-Code: {api_response.status_code} & Message: {api_response.text}")
        return api_response.json()
