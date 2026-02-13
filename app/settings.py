import environ

env = environ.Env()
environ.Env.read_env("C:\Projects\Task_Management_System\.env")

GITHUB_TOKEN = env("GITHUB_TOKEN")
GITHUB_REPO = env("GITHUB_REPO")
MONGO_URL = env("MONGO_URL")