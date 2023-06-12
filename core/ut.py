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


def set_python_path(conf, folder):
    os.system("echo $GITHUB_WORKSPACE")
    current_folder = cd.get_current_dir()
    print("CF:", current_folder)
    print("PYTHON PATH: ", conf.get("python_path", ""))
    if conf.get("python_path"):
        os.system(f"export PYTHONPATH={current_folder}:{current_folder}/{folder}:{conf['python_path']}")
    else:
        os.system(f"export PYTHONPATH={current_folder}:{current_folder}/{folder}")
    os.system("echo $PYTHONPATH")


def send_notification(notify):
    notify.send()
    if notify.coverage_status:
        return
    raise Exception("Test coverage not reach expectation")


def install_requirement(conf):
    for req_txt in conf["requirement"]:
        os.system(f"if [ -f {req_txt} ]; then pip install -r {req_txt}; fi")


def unit_test_executor():
    git_diff = get_git_diff()
    ut_conf = get_conf()
    notify = Postman()
    for _folder in git_diff:
        if ut_conf.get(_folder):
            install_requirement(ut_conf[_folder])
            set_python_path(ut_conf[_folder], _folder)
            with cd(_folder):
                subprocess.run(["nosetests", "-x", "--with-coverage", "--cover-erase", "--cover-package=.", "--cover-tests", "--cover-xml"])
                notify.bulk_action(cd.get_current_dir(), ut_conf[_folder]["coverage"])
    send_notification(notify)
