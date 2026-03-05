import os
import requests
import sys

event = os.getenv("GITHUB_EVENT_NAME")
actor = os.getenv("GITHUB_ACTOR")
repo = os.getenv("GITHUB_REPOSITORY")
token = os.getenv("GITHUB_TOKEN")

title = f"Workflow Event: {event}"

body = f"""
### Repository Event Detected

Event: {event}
Actor: {actor}
Repository: {repo}

This issue was automatically created by the workflow.
"""

url = f"https://api.github.com/repos/{repo}/issues"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

data = {
    "title": title,
    "body": body
}

requests.post(url, headers=headers, json=data)