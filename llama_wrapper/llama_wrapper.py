"""
Wrapper for interacting with the Llama trained models via the Replicate API.
"""

import datetime
import random
import time
import nltk
import requests
from colorama import Fore, init
from .constants import (
    API_URL,
    DEFAULT_HEADERS,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_TOP_P,
)
from .validator import PromptDataValidator

init(autoreset=True)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")


class LlamaWrapper:
    """
    A Python module for interacting with the Meta Llama models trained via Replicate's API.
    """

    def __init__(
        self,
        headers: dict = None,
        user_agents: list[str] = None,
        proxies: list[str] = None,
    ) -> None:
        """
        Initialize the LlamaWrapper object.

        Args:
            headers (dict): Custom HTTP headers for API requests. Defaults to DEFAULT_HEADERS.
            user_agents (list[str]): List of rotating user agents taken randomly.
            proxies (list[str]): List of proxies allowed for API requests. Only 'http' and 'https' protocols are supported.
        """
        self.user_agents = user_agents
        self.proxies = proxies
        self.headers = headers if headers else DEFAULT_HEADERS

    def prompt(
        self,
        message: str,
        model: str = DEFAULT_MODEL,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        top_p: float = DEFAULT_TOP_P,
    ) -> dict[str, datetime.timedelta, int, float]:
        """
        Generate a response from the Llama API based on the provided prompt.

        Args:
            message (str): The prompt message to generate a response for.
            model (str): The model to use for generating the response. Defaults to "meta/llama-2-70b-chat".
            max_tokens (int): The maximum number of tokens in the generated response. Defaults to 300.
            temperature (float): Controls the randomness of the response generation. Defaults to 0.0.
            top_p (float): Controls the diversity of tokens considered during generation. Defaults to 0.0.

        Returns:
            dict: A dictionary containing the following information:
                "response" (str): The generated response from the Llama API.
                "response_time" (datetime.timedelta): The time taken to receive the response.
        """
        PromptDataValidator(message, model, max_tokens, temperature, top_p)
        start_time = time.time()
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
            if self.user_agents:
                user_agent = random.choice(self.user_agents)
                self.headers["User-Agent"] = user_agent
            proxies = {}
            if self.proxies:
                proxy = random.choice(self.proxies)
                proxies = {proxy.split("//")[0]: proxy}

            response = requests.post(
                API_URL, headers=self.headers, json=data, proxies=proxies
            )

            if response.status_code == 200:
                response_llama_str = response.text
                end_time = time.time()
                response_time = end_time - start_time
                response_time_formatted = datetime.timedelta(seconds=response_time)

                response_llama = {
                    "response": response_llama_str,
                    "response_time": response_time_formatted,
                }

                return response_llama

            elif response.status_code == 403:
                raise requests.HTTPError(
                    f"{Fore.RED}You have probably been blocked by CloudFlare. Verify here: https://www.llama2.ai/"
                )
            else:
                raise Exception(
                    f"{Fore.RED}No response received - Status code: {response.status_code}, Reason: {response.reason}"
                )
        except requests.ConnectionError as e:
            raise Exception(
                f"{Fore.RED}A connection error occurred - Details: {str(e)}"
            )
        except requests.Timeout as e:
            raise Exception(
                f"{Fore.YELLOW}A timeout error occurred - Details: {str(e)}"
            )
        except Exception as e:
            raise Exception(f"{Fore.RED}An unexpected error occurred: {str(e)}")

    @staticmethod
    def get_tokens_stats(
        text: str, response_time: datetime.timedelta
    ) -> dict[int, float]:
        """
        Calculate token statistics from the provided text and response time.

        Args:
            text (str): The text to analyze for token statistics.
            response_time (datetime.timedelta): The time taken to generate the response.

        Returns:
            dict: A dictionary containing token statistics:
                "total_tokens" (int): The total number of tokens in the generated response.
                "token_rate" (float): The rate of token generation (tokens per second).
        """
        total_tokens: int = len(nltk.word_tokenize(text))
        token_rate: float = total_tokens / response_time.total_seconds()

        tokens_stats = {"total_tokens": total_tokens, "token_rate": token_rate}

        return tokens_stats
