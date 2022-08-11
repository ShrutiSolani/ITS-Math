from datetime import datetime
from cryptography.fernet import Fernet
from github import Github
from github.InputGitAuthor import InputGitAuthor
from decouple import config


class Log:
    def __init__(self):
        pass

    def log_entry(self, message):
        try:
            token = config('GITHUB_TOKEN')
            key = config('CRYPT_KEY')
            fernet = Fernet(bytes(key, 'utf-8'))
            token = fernet.decrypt(bytes(token, 'utf-8')).decode()
            file_path = config('LOG_FILE')
            g = Github(token)
            repo = g.get_repo(config('GITHUB_REPO'))
            branch = config('GITHUB_BRANCH')
            file = repo.get_contents(file_path, ref=branch)
            data = file.decoded_content.decode("utf-8")
            entry = str(datetime.now()) + '|' + message
            data += "\n" + entry
            # author = InputGitAuthor(
            #     config('GITHUB_USERNAME'),
            #     config('GITHUB_EMAIL')
            # )
            # contents = repo.get_contents(file_path, ref=branch)
            # repo.update_file(contents.path, "log entry", data, contents.sha, branch=branch, author=author)
        except Exception as e:
            print(e)
