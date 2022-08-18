


class Constant:
    COMMAND_API = "{domain}/repos/{git_repo}/commits/{commit_id}/comments"
    PAYLOAD_TEMPLATE = "<table><thead><tr><td>Total Lines</td><td>Covered</td><td>Coverage</td></tr></thead>" \
                       "<tbody><tr><td>{lines}</td><td>{covered}</td><td>{coverage} %</td></tr></tbody></table>"
