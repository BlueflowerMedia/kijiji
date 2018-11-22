from subprocess import Popen, PIPE
from subprocess import call

# Writes logs to log.txt
def logger(log):
    with open("log.txt", "a") as myfile:
        myfile.write(log)
        print(log)

# main function
def adPoster(ad_file, repost=True):
    # call(["python", "kijiji_repost_headless", "repost", ad_file])
    if (repost==True):
        p = Popen(["python", "kijiji_repost_headless", "repost", ad_file], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        # p = Popen(["echo","repost"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    else:
        p = Popen(["python", "kijiji_repost_headless", "post", ad_file], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        # p = Popen(["echo","post"], stdin=PIPE, stdout=PIPE, stderr=PIPE)

    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    rc = p.returncode

    # logging stdout
    logger("ADPOSTER OUTPUTS:")
    for line in output.decode("ascii").split('\n'):
        logger(line)

    # logging stderr
    logger("ADPOSTER ERROR: ")
    for line in err.decode("ascii").split('\n'):
        logger(line)

    return rc
