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
        self.payload = ""
        self.coverage_status = True
        self.set_authorized_header()

    def set_header(self, key, value):
        self.headers[key] = value

    def set_authorized_header(self):
        self.headers[NotificationConstant.AUTHORIZATION] = f"f{NotificationConstant.BEARER} {self.token}"

    def get_coverage(self, _dir):
        """return lines, covered, coverage """
        return coverage_export(_dir)

    def add_payload(self, lines, covered, coverage):
        self.payload += NotificationConstant.PAYLOAD_TEMPLATE.format(lines=lines, covered=covered, coverage=coverage)

    def bulk_action(self, _dir, ex_coverage):
        lines, covered, coverage = self.get_coverage(_dir)
        self.add_payload(lines, covered, coverage)
        if coverage < ex_coverage:
            self.coverage_status = False

    def payload_constructor(self, _dir):
        lines, covered, coverage = coverage_export(_dir)
        return coverage, {NotificationConstant.BODY: NotificationConstant.PAYLOAD_TEMPLATE.format(lines=lines, covered=covered, coverage=coverage)}

    def send(self):
        requests.post(NotificationConstant.COMMAND_API.format(domain=self.api_domain, git_repo=self.repo,
                                                             commit_id=self.commit_id), headers=self.headers,
                                 data=json.dumps({NotificationConstant.BODY: self.payload}))
