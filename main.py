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

# Fetch recent event activity from username
#----------------------------------------------------------------------------------------------------------------------#
def get_recent_activity(username):
    """Fetches the recent activity of the provided username"""
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url) # Get request for the API url
    if response.status_code == 200:
        github_data = response.json()
        events = github_data
        for event in events:
            if event['type'] == "CreateEvent": # Lists all CreateEvent actions taken recently by user
                rich_print(f"{username} created event: {event['payload']['ref_type']} {event['payload']['ref']}")
    else:
        print(f"\033[1;31mPlease enter a valid username.\0330m")




