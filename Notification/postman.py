import requests
import json
import os

from Notification import Constant
from util.coverage_parser import coverage_export


class Postman:
    def __init__(self):
        self.headers = {}
        self.token = os.getenv("github_token")
        self.repo = os.getenv("github_repository")
        self.api_domain = "https://api.github.com"
        self.commit_id = os.getenv("commit_id")
        self.ex_coverage = int(os.getenv("expect_coverage", 90))

    def set_header(self, key, value):
        self.headers[key] = value

    def payload_constructor(self, dir):
        self.set_header("Authorization", "Bearer " + self.token)
        lines, covered, coverage = coverage_export(dir)
        return coverage, {"body": Constant.PAYLOAD_TEMPLATE.format(lines=lines, covered=covered, coverage=coverage)}

    def send(self, _dir):
        coverage, payload = self.payload_constructor(_dir)
        print(Constant.COMMAND_API.format(domain=self.api_domain, git_repo=self.repo, commit_id=self.commit_id),
                      self.headers, payload)
        response = requests.post(Constant.COMMAND_API.format(domain=self.api_domain, git_repo=self.repo, commit_id=self.commit_id),
                      headers=self.headers, data=json.dumps(payload))
        print(response.text)
        return coverage>=self.ex_coverage 
