"""
Constants for interacting with the Llama trained models via the Replicate API.
"""

from data_types import DecimalNumber


API_URL = "https://www.llama2.ai/api"

MODELS = [
    "meta/meta-llama-3-70b-instruct",
    "meta/meta-llama-3-8b-instruct",
    "meta/llama-2-70b-chat",
    "meta/llama-2-13b-chat",
    "meta/llama-2-7b-chat",
]

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Host": "www.llama2.ai",
    "Accept-Encoding": "gzip, deflate, br",
}

DEFAULT_MODEL = "meta/llama-2-70b-chat"

MIN_TOKENS = 1
MAX_TOKENS = 4096
DEFAULT_MAX_TOKENS = 300

MIN_TEMPERATURE = DecimalNumber(0, 0)
MAX_TEMPERATURE = DecimalNumber(5, 0)
DEFAULT_TEMPERATURE = DecimalNumber(0, 75)

MIN_TOP_P = DecimalNumber(0, 0)
MAX_TOP_P = DecimalNumber(5, 0)
DEFAULT_TOP_P = DecimalNumber(0, 9)
