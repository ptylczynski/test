import os
import subprocess
from threading import Thread

import git


class GeneratorExecutor(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("Thread runs")
        change_log = open("CHANGELOG.txt", "w+")
        subprocess.call('git-changelog . -s basic -t keepachangelog'.split(' '), stdout=change_log)
        change_log.close()

        repo = git.Repo(os.getcwd())
        repo.git.add(update=True)
        repo.index.commit('Changelog commit message')
        origin = repo.remote(name='origin')
        origin.push()