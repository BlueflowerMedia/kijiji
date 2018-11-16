# from subprocess import Popen, PIPE
from subprocess import call

def adRunner(jobID):
    jobFile = "ad" + str(jobID) + "/ad" + str(jobID) + ".yml"
    call(["python", "kijiji_repost_headless", "repost", jobFile])
    # p = Popen(["python", "kijiji_repost_headless", "repost", jobFile], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    # output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    # rc = p.returncode
    # return (output, err)
