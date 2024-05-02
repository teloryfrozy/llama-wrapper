import unittest
from src.main import LlamaWrapper


class TestLlamaWrapper(unittest.TestCase):
    def test_prompt(self):
        llama_ai = LlamaWrapper()
        response_llama = llama_ai.prompt("How are you today?")
        self.assertIsInstance(response_llama, str)


if __name__ == "__main__":
    unittest.main()
