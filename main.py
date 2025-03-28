import requests
import sys
from rich import print as rich_print

# TODO 1. Have user provide GitHub username as an argument when running the CLI
# TODO 2. Fetch recent activity of GH user using API
# TODO 3. Display the fetched activity in the terminal, using JSON
# TODO 4. Handle errors gracefully
# TODO 5. Filter by Event type
# TODO 6. Cache fetched data
github_api_url = "https://api.github.com/users" # GitHub API URL reference

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
            else:
                rich_print(f"{event['type']}")
    else:
        print(f"Failed to retrieve user data: {response.status_code}")

