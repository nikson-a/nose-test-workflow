import os
import sys
import subprocess
from notification.postman import Postman
from util.change_directory import ChangeDirectory as cd
from util.coverage_parser import coverage_export
import json
from util.git_engine import get_git_diff


def get_conf():
    with open("nose_test_workflow_conf.json", "r") as conf_file:
        conf = json.loads(conf_file.read())
    return conf


def unit_test_executor():
    git_diff = get_git_diff()
    ut_conf = get_conf()
    block = True
    for _conf in ut_conf:
        _cd = cd.get_current_dir()
        os.system("export PYTHONPATH=$PYTHONPATH:%s" %_cd + _conf["python_path"])
        os.system("echo $PYTHONPATH")
        if _conf.get("path").split("/")[0] in git_diff:
            with cd(_conf.get("path")):
                os.system(f"if [ -f {_conf['requirement']} ]; then pip install -r {_conf['requirement']}; fi")
                subprocess.run(["nosetests", "-x", "--with-coverage", "--cover-erase", "--cover-package=.", "--cover-tests", "--cover-xml"])
                notify = Postman()
                if not notify.send(cd.get_current_dir()):
                    block = False
    if not block:
        raise Exception("Test coverage not reach expection")
