# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from util.change_directory import ChangeDirectory as cd
import os
from core.ut import unit_test_executor


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))
    with cd("./"):
        unit_test_executor()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
