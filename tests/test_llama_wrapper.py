"""
Unit tests for LlamaWrapper and PromptDataValidator classes.
"""

import io
import unittest
import os
import sys
from colorama import Fore, init

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(project_root, "..")))
sys.stdout = io.StringIO()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.constants import (
    DEFAULT_MAX_TOKENS,
    DEFAULT_MESSAGE,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_TOP_P,
)
from src.llama_wrapper import LlamaWrapper
from src.validator import PromptDataValidator

init(autoreset=True)


class TestLlamaWrapper(unittest.TestCase):
    """Test cases for LlamaWrapper class and PromptDataValidator."""

    def setUp(self):
        """Initialize common objects or configurations."""
        self.llama_ai = LlamaWrapper()
        self.prompt_validator = PromptDataValidator(
            message=DEFAULT_MESSAGE,
            model=DEFAULT_MODEL,
            max_tokens=DEFAULT_MAX_TOKENS,
            temperature=DEFAULT_TEMPERATURE,
            top_p=DEFAULT_TOP_P,
        )

    def test_model_validation(self):
        """Test validation of model parameter."""
        is_valid = self.prompt_validator.verify_model(self.prompt_validator.model)
        self.assertTrue(
            is_valid, f"{Fore.RED}Model validation failed: Expected model to be valid."
        )
        result = self.prompt_validator.verify_model("gpt-3.5-turbo")
        self.assertFalse(
            result,
            f"{Fore.RED}Model validation failed: Expected model validation to fail for invalid input.",
        )

    def test_max_tokens_validation(self):
        """Test validation of max_tokens parameter."""
        is_valid = self.prompt_validator.verify_max_tokens(
            self.prompt_validator.max_tokens
        )
        self.assertTrue(
            is_valid,
            f"{Fore.RED}Max tokens validation failed: Expected max_tokens to be valid.",
        )
        result = self.prompt_validator.verify_max_tokens(4097)
        self.assertFalse(
            result,
            f"{Fore.RED}Max tokens validation failed: Expected max_tokens validation to fail for invalid input.",
        )

    def test_temperature_validation(self):
        """Test validation of temperature parameter."""
        is_valid = self.prompt_validator.verify_temperature(
            self.prompt_validator.temperature
        )
        self.assertTrue(
            is_valid,
            f"{Fore.RED}Temperature validation failed: Expected temperature to be valid.",
        )
        result = self.prompt_validator.verify_temperature(1)
        self.assertFalse(
            result,
            f"{Fore.RED}Temperature validation failed: Expected temperature validation to fail for invalid input.",
        )

    def test_top_p_validation(self):
        """Test validation of top_p parameter."""
        is_valid = self.prompt_validator.verify_top_p(self.prompt_validator.top_p)
        self.assertTrue(
            is_valid, f"{Fore.RED}Top P validation failed: Expected top_p to be valid."
        )
        result = self.prompt_validator.verify_top_p(1)
        self.assertFalse(
            result,
            f"{Fore.RED}Top P validation failed: Expected top_p validation to fail for invalid input.",
        )


if __name__ == "__main__":
    unittest.main()
