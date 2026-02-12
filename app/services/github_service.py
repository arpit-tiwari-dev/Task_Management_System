import environ
from github import Github

env = environ.Env()
environ.Env.read_env("C:\Projects\Task_Management_System\.env")

class GithubService:
    def __init__(self):
        token = env("GITHUB_TOKEN")
        self.client = Github(token)
        repo_name = env("GITHUB_REPO")
        self.repo = self.client.get_repo(repo_name)

    def create_issue(self, title: str, body: str):
        issue = self.repo.create_issue(title=title, body=body)
        return issue.number
