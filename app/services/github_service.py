from github import Github

from app.settings import GITHUB_REPO, GITHUB_TOKEN

class GithubService:
    def __init__(self):
        token = GITHUB_TOKEN
        self.client = Github(token)
        repo_name = GITHUB_REPO
        self.repo = self.client.get_repo(repo_name)

    def create_issue(self, title: str, body: str):
        issue = self.repo.create_issue(title=title, body=body)
        return issue.number
