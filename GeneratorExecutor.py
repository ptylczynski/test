import os
import subprocess
from threading import Thread

import git

import Config


class GeneratorExecutor(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("Generating / updating new changelog")
        change_log = open(Config.CHANGELOG_NAME, "w+")
        subprocess.call('git-changelog . -s basic -t keepachangelog'.split(' '), stdout=change_log)
        change_log.close()

        repo = git.Repo(Config.REPOSITORY_ROOT)
        repo.git.add(update=True)
        repo.index.commit(Config.COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push(Config.BRANCH_TO_WATCH)
