import subprocess
from threading import Thread


class Executor(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("Thread runs")
        change_log = open("CHANGELOG.txt", "w+")
        subprocess.call('git-changelog . -s basic -t keepachangelog'.split(' '), stdout=change_log)