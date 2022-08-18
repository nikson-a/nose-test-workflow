import git


def get_git_diff():
    repo = git.Repo(".")
    _diff = repo.git.diff("HEAD^..HEAD",  "--name-only")
    return list(set([_dir.split("/")[0] for _dir in _diff.split("\n")]))
