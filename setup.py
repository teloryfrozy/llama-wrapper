import setuptools

setuptools.setup(
    name="llama_wrapper",
    author="teloryfrozy",
    description="🦙 A Python module for interacting with the Meta Llama models trained via Replicate's API. 🔓",
    keywords="reverse-engineering, meta, replicate, llm, llama2, llama3",
    url="https://github.com/teloryfrozy/llama-wrapper/",
    packages=setuptools.find_packages(),
    project_urls={
        "GitHub": "https://github.com/teloryfrozy/llama-wrapper",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
