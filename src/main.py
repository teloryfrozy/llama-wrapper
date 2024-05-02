import requests
from src.constants import API_URL, DEFAULT_HEADERS


class LlamaWrapper:
    """
    A Python module for interacting with the Meta Llama models trained via Replicate's API.
    """

    def __init__(self, headers: dict = None) -> None:
        """
        Initialize the LlamaWrapper object.

        Args:
            headers (dict): Custom HTTP headers for API requests. Defaults to DEFAULT_HEADERS.
        """
        self.headers = headers if headers else DEFAULT_HEADERS

    def prompt(
        self,
        message: str,
        model: str = "meta/llama-2-70b-chat",
        max_tokens: int = 300,
        temperature: float = 0.0,
        top_p: float = 0.0,
    ) -> str:
        """
        Generate a response from the Llama API based on the provided prompt.

        Args:
            message (str): The prompt message to generate a response for.
            model (str): The model to use for generating the response. Defaults to "meta/llama-2-70b-chat".
            max_tokens (int): The maximum number of tokens in the generated response. Defaults to 300.
            temperature (float): Controls the randomness of the response generation. Defaults to 0.0.
            top_p (float): Controls the diversity of tokens considered during generation. Defaults to 0.0.

        Returns:
            str: The generated response from the Llama API.
        """
        data = {
            "audio": None,
            "image": None,
            "maxTokens": max_tokens,
            "model": model,
            "prompt": message,
            "temperature": temperature,
            "topP": top_p,
        }

        try:
            response = requests.post(API_URL, headers=self.headers, json=data)

            if response.status_code == 200:
                response_llama = response.content.decode("utf-8")
                return response_llama
            else:
                raise Exception(
                    f"No response received - Status code: {response.status_code}, Reason: {response.reason}"
                )
        except requests.ConnectionError as e:
            raise Exception(f"A connection error occurred - Details: {str(e)}")
        except requests.Timeout as e:
            raise Exception(f"A timeout error occurred - Details: {str(e)}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")
