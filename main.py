import socket
from time import sleep

import git

import Config
from GeneratorExecutor import GeneratorExecutor


class AutoChangeLogServer:
    def __init__(self):
        while True:
            print("Pulling branch " + Config.BRANCH_TO_WATCH)
            repo = git.Repo(Config.REPOSITORY_ROOT)
            o = repo.remotes.origin
            o.pull(Config.BRANCH_TO_WATCH)
            GeneratorExecutor().start()
            sleep(10)


if __name__ == "__main__":
    AutoChangeLogServer()