

class NotificationConstant:
    GIT_API_DOMAIN = "https://api.github.com"
    COMMAND_API = "{domain}/repos/{git_repo}/pulls/{pull_number}/comments"
    PAYLOAD_TEMPLATE = "<table><thead><tr><td>Number of Lines</td><td>Number of Lines Covered</td><td>Coverage (%)</td></tr></thead>" \
                       "<tbody><tr><td>{lines}</td><td>{covered}</td><td>{coverage} %</td></tr></tbody></table>"
    GITHUB_TOKEN = "github_token"
    GITHUB_REPOSITORY = "github_repository"
    PR_NUMBER = "PR_NUMBER"
    COMMIT_ID = "commit_id"
    EXPECT_COVERAGE = "expect_coverage"
    AUTHORIZATION = "Authorization"
    BEARER = "Bearer"
    BODY = "body"
