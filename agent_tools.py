import os
import requests
from langchain.agents import tool
from dotenv import load_dotenv

load_dotenv()

@tool(description="Search the web and return the top snippet.")
def web_search(query: str) -> str:
    key = os.getenv("SERPER_API_KEY")
    if not key:
        return "Error: Missing API key"
    resp = requests.post(
        "https://google.serper.dev/search",
        headers={"X-API-KEY": key},
        json={"q": query},
    )
    resp.raise_for_status()
    organic = resp.json().get("organic", [])
    return organic[0].get("snippet", "No snippet.") if organic else "No snippet."