import os


class ChangeDirectory:
    """Context manager for changing the current working directory"""
    def __init__(self, folder_name):
        self.work_dir = os.path.expanduser(folder_name)
        self.root_dir = os.getcwd()

    @staticmethod
    def get_current_dir():
        return os.getcwd()

    def __enter__(self):
        os.chdir(self.work_dir)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.root_dir)
