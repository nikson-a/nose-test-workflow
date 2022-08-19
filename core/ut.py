import os
import sys
import subprocess
from Notification.postman import Postman
from util.change_directory import ChangeDirectory as cd
from util.coverage_parser import coverage_export
from util.git_engine import get_git_diff


def unit_test_executor():
    git_diff = get_git_diff()
    print(git_diff)
    for dir in git_diff:
        # _cd = cd.get_current_dir()
        # print(_cd, type(_cd))
        # os.system("export PYTHONPATH=$PYTHONPATH:%s" %_cd)
        # sys.path.append(cd.get_current_dir())
        # os.system("echo $PYTHONPATH")
        if not dir.startswith(".") and not os.path.isfile(os.getcwd() + "/" + dir):
            with cd(dir):
                os.system("if [ -f requirements.txt ]; then pip install -r requirements.txt; fi")
                subprocess.run(["nosetests", "-x", "--with-coverage", "--cover-erase", "--cover-package=.", "--cover-tests",
                                "--cover-xml"])
                # print(coverage_export(cd.get_current_dir()))
                notify = Postman()
                notify.send(cd.get_current_dir())
