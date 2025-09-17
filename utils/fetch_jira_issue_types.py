import os
import requests
from requests.auth import HTTPBasicAuth

def fetch_jira_issue_types():
    url = f"{os.environ['JIRA_INSTANCE_URL']}/rest/api/3/issuetype"
    auth = HTTPBasicAuth(os.environ["JIRA_USERNAME"], os.environ["JIRA_API_TOKEN"])
    response = requests.get(url, auth=auth)
    response.raise_for_status()
    types = [t["name"] for t in response.json()]
    return types