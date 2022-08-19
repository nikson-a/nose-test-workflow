from util.change_directory import ChangeDirectory as cd
import os
from core.ut import unit_test_executor


if __name__ == '__main__':
    # for name, value in os.environ.items():
    #     print("{0}: {1}".format(name, value))
    with cd("./"):
        unit_test_executor()
        
