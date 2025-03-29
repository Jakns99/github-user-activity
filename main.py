import requests
import sys
from rich import print as rich_print
from dataclasses import dataclass
from requests_cache import CachedSession

# TODO 1. Have user provide GitHub username as an argument when running the CLI
# TODO 2. Fetch recent activity of GH user using API (DONE)
# TODO 3. Display the fetched activity in the terminal, using JSON (DONE)
# TODO 4. Handle errors gracefully
# TODO 5. Filter by Event type
# TODO 6. Cache fetched data
github_api_url = "https://api.github.com/users" # GitHub API URL reference

session = CachedSession(
    cache_name='github_cache',
    backend='sqlite',
    expire_after=3600,  # Cache for 1 hour
)

@dataclass
class User:
    """Dataclass to represent a GitHub user"""
    username: str
    events_url: str

 # Fetch recent event activity from username using api link
#----------------------------------------------------------------------------------------------------------------------#
def get_recent_activity(username):
    """Fetches the recent activity of the provided username"""
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        events = response.json()
        for event in events:
            if event['type'] == "CreateEvent": # Lists recent CreateEvents by the user
                rich_print(f"{username} created {event['payload']['ref_type']} {event['payload']['ref']}")
            elif event['type'] == "PushEvent": # Lists recent code pushes by user
                rich_print(f"{username} pushed new code to {event['repo']['name']}")
            elif event['type'] == "PullRequestEvent": # List recent pull requests by user
                rich_print(f"{username} created pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == "ForkEvent": # Lists recent forks by user
                rich_print(f"{username} forked {event['repo']['name']}")
            elif event['type'] == "WatchEvent": # Lists recent stars by user
                rich_print(f"{username} starred {event['repo']['name']}")
            elif event['type'] == "IssueCommentEvent": # Lists recent comments by user
                rich_print(f"{username} commented on issue {event['payload']['issue']['number']} in {event['repo']['name']}")
            else:
                rich_print(f"{event['type']}")
    else:
        print(f"Failed to retrieve user data: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) > 1: # If user provides a username
        get_recent_activity(sys.argv[1]) # Fetches the recent activity of the provided username
    else:
        print("Error, username not found, please provide a valid GitHub username.")