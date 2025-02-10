import requests
from dotenv import load_dotenv
import os
import sys

# Load GitHub token from .env
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

OWNER = "microsoft"
REPO = "terminal"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}
API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"

# Set the default encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def fetch_commits():
    page = 1

    while True:
        response = requests.get(API_URL, params={"per_page": 100, "page": page})

        if response.status_code == 403:
            print("API rate limit exceeded. Try again later.")
            break
        elif response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            break

        commit_data = response.json()
        if not commit_data:
            break  # No more commits

        for idx, commit in enumerate(commit_data, start=1):
            try:
                print(f"Message: {commit["commit"]["message"]}")
                print(f"Author: {commit["commit"]["author"]["name"]}")
                print("-" * 40)
            except UnicodeEncodeError:
                print(f"Message {idx}: Encoding error occurred while printing commit.")
                continue 

        page += 1

if __name__ == "__main__":
    fetch_commits()
