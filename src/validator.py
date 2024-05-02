"""
Data type and content validator for Llama trained models.
"""

from constants import (
    MAX_TEMPERATURE,
    MAX_TOKENS,
    MAX_TOP_P,
    MIN_TEMPERATURE,
    MIN_TOKENS,
    MIN_TOP_P,
    MODELS,
)
from data_types import DecimalNumber


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
                self.verify_model(),
                self.verify_max_tokens(),
                self.verify_temperature(),
                self.verify_top_p(),
            ]
        ):
            raise ValueError("Invalid prompt data")

    def verify_model(self) -> bool:
        """
        Verify if the provided model is valid.

        Returns:
            bool: True if the model is valid, False otherwise.
        """
        if not isinstance(self.model, str):
            raise TypeError("Model must be a string")
        if self.model not in MODELS:
            return False
        return True

    def verify_temperature(self) -> bool:
        """
        Verify if the provided temperature is within the valid range.

        Returns:
            bool: True if the temperature is valid, False otherwise.
        """
        if not isinstance(self.temperature, DecimalNumber):
            raise TypeError("Temperature must be a DecimalNumber object")
        if not (MIN_TEMPERATURE <= self.temperature <= MAX_TEMPERATURE):
            return False
        return True

    def verify_max_tokens(self) -> bool:
        """
        Verify if the provided max_tokens is within the valid range.

        Returns:
            bool: True if the max_tokens is valid, False otherwise.
        """
        if not isinstance(self.max_tokens, int):
            raise TypeError("Max tokens must be an integer")
        if not (MIN_TOKENS <= self.max_tokens <= MAX_TOKENS):
            return False
        return True

    def verify_top_p(self) -> bool:
        """
        Verify if the provided top_p is within the valid range.

        Returns:
            bool: True if the top_p is valid, False otherwise.
        """
        if not isinstance(self.top_p, DecimalNumber):
            raise TypeError("Top P must be a DecimalNumber object")
        if not (MIN_TOP_P <= self.top_p <= MAX_TOP_P):
            return False
        return True
