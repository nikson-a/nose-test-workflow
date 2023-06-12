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
    # env_file = os.getenv('GITHUB_ENV')
    current_folder = cd.get_current_dir()
    os.system('echo "action_state=yellow" >> "$GITHUB_ENV"')
    # with open(env_file, "a") as fp:
        # myfile.write("MY_VAR=MY_VALUE")
    os.system(f'echo "PYTHON_PATH={current_folder}:{current_folder}/{folder}:" >> "$GITHUB_ENV"')
    if conf.get("python_path"):
        python_path = conf['python_path']
        # fp.write(f"PYTHONPATH={current_folder}:{current_folder}/{folder}:{python_path}")
        os.system(f'echo "PYTHONPATH={current_folder}:{current_folder}/{folder}:{python_path}" >> "$GITHUB_ENV"')
    else:
        # fp.write(f"PYTHONPATH={current_folder}:{current_folder}/{folder}")
        os.system(f'echo "PYTHONPATH={current_folder}:{current_folder}/{folder}" >> "$GITHUB_ENV"')
    os.system("echo $PYTHONPATH")
    os.system("echo $PYTHON_PATH")
    os.system("echo $action_state")


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
            set_python_path(ut_conf[_folder], _folder)
            install_requirement(ut_conf[_folder])
            with cd(_folder):
                subprocess.run(["nosetests", "-x", "--with-coverage", "--cover-erase", "--cover-package=.", "--cover-tests", "--cover-xml"])
                notify.bulk_action(cd.get_current_dir(), ut_conf[_folder]["coverage"])
    send_notification(notify)
