import requests
import json
import os

from notification import NotificationConstant
from util.coverage_parser import coverage_export


class Postman:
    def __init__(self):
        self.headers = {}
        self.token = os.getenv(NotificationConstant.GITHUB_TOKEN)
        self.repo = os.getenv(NotificationConstant.GITHUB_REPOSITORY)
        self.api_domain = NotificationConstant.GIT_API_DOMAIN
        self.commit_id = os.getenv(NotificationConstant.COMMIT_ID)
        self.ex_coverage = int(os.getenv(NotificationConstant.EXPECT_COVERAGE, 90))

    def set_header(self, key, value):
        self.headers[key] = value

    def payload_constructor(self, _dir):
        self.set_header(NotificationConstant.AUTHORIZATION, f"f{Constant.BEARER} {self.token}")
        lines, covered, coverage = coverage_export(_dir)
        return coverage, {NotificationConstant.BODY: NotificationConstant.PAYLOAD_TEMPLATE.format(lines=lines, covered=covered, coverage=coverage)}

    def send(self, _dir):
        coverage, payload = self.payload_constructor(_dir)
        requests.post(NotificationConstant.COMMAND_API.format(domain=self.api_domain, git_repo=self.repo,
                                                             commit_id=self.commit_id), headers=self.headers,
                                 data=json.dumps(payload))
        return coverage >= self.ex_coverage
