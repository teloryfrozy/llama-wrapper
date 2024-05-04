"""
Data type and content validator for Llama trained models.
"""

from colorama import Fore, init
from .constants import (
    MAX_TEMPERATURE,
    MAX_TOKENS,
    MAX_TOP_P,
    MIN_TEMPERATURE,
    MIN_TOKENS,
    MIN_TOP_P,
    MODELS,
)

init(autoreset=True)


class PromptDataValidator:
    """Validates the integrity and consistency of prompt data."""

    def __init__(
        self,
        message: str,
        model: str,
        max_tokens: int,
        temperature: float,
        top_p: float,
    ) -> None:
        """
        Initialize a PromptDataValidator object.

        Args:
            message (str): The message for the prompt.
            model (str): The model string.
            max_tokens (int): The maximum tokens.
            temperature (float): The temperature value.
            top_p (float): The top P value.
        """
        self.message = message
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.validate_prompt()

    def validate_prompt(self) -> None:
        """Verifies all prompt parameters."""
        if not all(
            [
                (self.model, self.verify_model),
                (self.max_tokens, self.verify_max_tokens),
                (self.temperature, self.verify_temperature),
                (self.top_p, self.verify_top_p),
            ],
        ):
            raise ValueError(f"{Fore.RED}Invalid prompt data")

    @staticmethod
    def verify_model(model: str) -> bool:
        """
        Verify if the provided model is valid.

        Returns:
            bool: True if the model is valid, False otherwise.
        """
        if not isinstance(model, str):
            print(TypeError(f"{Fore.RED}Model must be a string"))
            return False
        if model not in MODELS:
            print(
                f"{Fore.RED}Model: '{model}' is not allowed. List of allowed models: {MODELS}"
            )
            return False
        return True

    @staticmethod
    def verify_temperature(temperature: float) -> bool:
        """
        Verify if the provided 'temperature' value is within the valid range.

        Args:
            temperature (float): The 'temperature' value to be validated.

        Returns:
            bool: True if the 'temperature' is valid, False otherwise.
        """
        if not isinstance(temperature, float):
            print(TypeError(f"{Fore.RED}Temperature must be a float object"))
            return False
        if not (MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE):
            print(
                f"{Fore.RED}Invalid 'temperature': '{temperature}'. The allowed range is: {MIN_TEMPERATURE} to {MAX_TEMPERATURE}"
            )
            return False
        return True

    @staticmethod
    def verify_max_tokens(max_tokens: int) -> bool:
        """
        Verify if the provided 'max_tokens' value is within the valid range.

        Args:
            max_tokens (int): The 'max_tokens' value to be validated.

        Returns:
            bool: True if the 'max_tokens' is valid, False otherwise.
        """
        if not isinstance(max_tokens, int):
            print(TypeError(f"{Fore.RED}Max tokens must be an integer"))
            return False
        if not (MIN_TOKENS <= max_tokens <= MAX_TOKENS):
            print(
                f"{Fore.RED}Invalid 'max_tokens': '{max_tokens}'. The allowed range is: {MIN_TOKENS} to {MAX_TOKENS}"
            )
            return False
        return True

    @staticmethod
    def verify_top_p(top_p: float) -> bool:
        """
        Verify if the provided 'top_p' value is within the valid range.

        Args:
            top_p (float): The 'top_p' value to be validated.

        Returns:
            bool: True if the 'top_p' is valid, False otherwise.
        """
        if not isinstance(top_p, float):
            print(TypeError(f"{Fore.RED}'top_p' must be a float object"))
            return False
        if not (MIN_TOP_P <= top_p <= MAX_TOP_P):
            print(
                f"{Fore.RED}Invalid 'top_p': '{top_p}'. The allowed range is: {MIN_TOP_P} to {MAX_TOP_P}"
            )
            return False
        return True

    @staticmethod
    def verify_headers(headers: list[str]) -> bool:
        """
        Verify the integrity of header configurations.

        Args:
            headers (list): A list containing header configurations as strings.

        Returns:
            bool: True if the header configurations are valid, False otherwise.
        """
        if not isinstance(headers, list[str]):
            print(TypeError(f"{Fore.RED}'headers' must be a list containing strings"))
            return False
        return True

    @staticmethod
    def verify_proxies(proxies: list[str]) -> bool:
        """
        Verify the integrity of proxy configurations.

        Args:
            proxies (list): A list containing proxy endpoints.
                Each endpoint should be a string representing either an HTTP or HTTPS proxy.

        Returns:
            bool: True if the proxy configurations are valid, False otherwise.
        """
        if not isinstance(proxies, list[str]):
            print(TypeError(f"{Fore.RED}'proxies' must be a list"))
            return False
        return True
