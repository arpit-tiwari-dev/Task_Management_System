from github import Github

from app.settings import GITHUB_REPO, GITHUB_TOKEN
from app.db.mongo import task_collection

class GithubService:
    def __init__(self):
        token = GITHUB_TOKEN
        self.client = Github(token)
        repo_name = GITHUB_REPO
        self.repo = self.client.get_repo(repo_name)

    async def create_issue(self, task_id: str,title: str, body: str):
        issue = self.repo.create_issue(title=title, body=body)
        await task_collection.update_one(
            {"id":task_id},
            {"$set":{"external_reference_id":str(issue.number)}}
        )
