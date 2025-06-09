import yaml
from typing import Any, Dict, Type
from bs4 import BeautifulSoup
from httpx import Client
from pydantic import BaseModel
from pydantic_ai.models.groq import GroqModel
from pydantic_ai import Agent


def load_config(path: str = "configs/config.yaml") -> Dict[str, Any]:
    """Load model configuration from a YAML file.

    Args:
        path (str): Path to the YAML configuration file. Defaults to "config.yaml".

    Returns:
        Dict[str, Any]: A dictionary containing configuration values such as
                        model name, temperature, max_tokens, base_url, etc.
    """
    with open(path, "r") as f:
        return yaml.safe_load(f)


def fetch_html_text(url: str) -> str:
    """Fetches and cleans raw HTML text from a given URL.

    Args:
        url (str): The target URL to scrape.

    Returns:
        str: A single-line string containing the cleaned text content of the webpage.
             Newlines and carriage returns are removed to reduce token count.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/121.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.8",
    }
    with Client(headers=headers, timeout=20) as client:
        r = client.get(url)
        if r.status_code != 200:
            return f"ERROR: status {r.status_code}"
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.get_text().replace("\n", " ").replace("\r", " ")


def scrape(url: str, prompt_template: str, schema: Type[BaseModel]) -> BaseModel:
    """Scrapes a web page and extracts structured data using an LLM and a Pydantic schema.

    Args:
        url (str): The URL of the web page to scrape.
        prompt_template (str): A prompt template that includes a `{html}` placeholder
                               for the web page content.
        schema (Type[BaseModel]): A Pydantic model defining the structure of the expected output.

    Returns:
        BaseModel: An instance of the provided schema containing structured, validated data
                   extracted from the web page.
    """
    config = load_config()
    model = GroqModel(
        config["model"],
        # temperature=config.get("temperature", 0.7),
        # max_tokens=config.get("max_tokens", 128),
        # base_url=config.get("base_url"),
        # timeout=config.get("timeout", 30),
        # retry_count=config.get("retry_count", 3),
    )

    html = fetch_html_text(url)
    html_excerpt = html[:10000]
    prompt = prompt_template.format(html=html_excerpt)

    agent = Agent(model=model, output_type=schema)
    result = agent.run_sync(prompt)
    return result.output
