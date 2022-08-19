import requests
import os

from Notification import Constant
from util.coverage_parser import coverage_export


class Postman:
    def __init__(self):
        self.headers = {}
        self.token = os.getenv("GITHUB_TOKEN")
        self.repo = os.getenv("GITHUB_REPOSITORY")
        self.api_domain = os.getenv("github-api-domain", "https://api.github.com")
        self.commit_id = os.getenv("GITHUB_SHA")

    def set_header(self, key, value):
        self.headers[key] = value

    def payload_constructor(self, dir):
        self.set_header("Authorization", self.token)
        lines, covered, coverage = coverage_export(dir)
        return Constant.PAYLOAD_TEMPLATE.format(lines=lines, covered=covered, coverage=coverage)

    def send(self, _dir):
        payload = self.payload_constructor(_dir)
        print(Constant.COMMAND_API.format(domain=self.api_domain, git_repo=self.repo, commit_id=self.commit_id),
                      self.headers, payload)
        response = requests.post(Constant.COMMAND_API.format(domain=self.api_domain, git_repo=self.repo, commit_id=self.commit_id),
                      headers=self.headers, data=payload)
        print(response.text)
