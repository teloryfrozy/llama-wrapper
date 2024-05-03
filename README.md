# Python Wrapper For Replicate Trained Llama Models
🦙 A Python module for interacting with the Meta Llama models trained via Replicate's API. 🔓

## ⚠️ Disclaimer ⚠️
I do not personally use this module. It is intended for skill demonstration purposes only.

*This API reverse engineering project does not require any prior experience, except for understanding the basics of web development and API calls.*

## 🔑 Authentication
No API key is required to access the publicly available Llama models trained by Replicate.

## Features
- Prompt AI: Send a message to a llama LLM and get a response.
- Token Stats: Retrieve statistical data about LLM prompt performance.

## Installation
```bash
pip install llama-wrapper
```

## Examples of usage
```python
from llama_wrapper import LlamaWrapper

llama_wrapper = LlamaWrapper()
response_llama = llama_wrapper.prompt("Hello, Give me 3 short tips for my Junior Gen AI internship interview?")
print(response_llama["response"])
```
```bash
Here are three short tips to help you prepare for your Junior Gen AI internship interview:

1. **Be prepared to talk about your projects**: Make sure you can explain your projects in detail, including the problems you solved, the technologies you used, and the results you achieved.
2. **Show your passion for AI and machine learning**: Demonstrate your enthusiasm for AI and machine learning by sharing your thoughts on the latest developments in the field, and how you think AI and machine learning can be applied to real-world problems.
3. **Be prepared to ask thoughtful questions**: Come prepared with a list of thoughtful questions to ask the interviewer. This will show that you are interested in the company and the role, and that you are willing to learn and grow.

I hope these tips are helpful! Good luck with your interview!
```
---
```python
llama_wrapper = LlamaWrapper()
response_llama = llama_wrapper.prompt("Hi, give me 3 guidelines on how to become rich?")
print(llama_wrapper.get_tokens_stats(response_llama["response"], response_llama["response_time"]))
```
```bash
{'total_tokens': 208, 'token_rate': 97.8343795654084}
```

## Contributing
- Open pull requests for documentation improvements, additional features, or bug fixes.
- Report issues on the official repository, and we'll do our best to address them.
