"""
Constants for interacting with Llama trained models Replicate API.
"""

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
