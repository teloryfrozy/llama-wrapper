import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.validator import PromptDataValidator
from src.main import LlamaWrapper


class TestLlamaWrapper(unittest.TestCase):
    def test_prompt(self):
        llama_ai = LlamaWrapper()
        response_llama = llama_ai.prompt("How are you today?")
        self.assertIsInstance(response_llama, str)

    def test_model(self):
        result = PromptDataValidator().verify_model("gpt-3.5-turbo")
        self.assertFalse(result)
        result = PromptDataValidator().verify_model("meta/llama-2-70b-chat")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
