import schedule
import time
import datetime
from adRunner import *

# Writes logs to log.txt
def logger(log):
    with open("log.txt", "a") as myfile:
        myfile.write(log)

# Runs job batches with functions in adRunner.py
def runJobs(job_list):
    logger(str(datetime.datetime.now()))
    for jobID in job_list:
        adRunner(jobID)
        # log = str(adRunner(jobID)) + "\n"
        # logger(log[0])
        # logger(log[1])
    logger("\n")

# scheduler
# schedule.every(60).minutes.do(runJobs,[1,2])
# time.sleep(1200)
# schedule.every(60).minutes.do(runJobs,[3,4])
# time.sleep(1200)
# schedule.every(60).minutes.do(runJobs,[5,6])




schedule.every(30).minutes.do(runJobs,[1])
time.sleep(900)
schedule.every(30).minutes.do(runJobs,[3])
while True:
    schedule.run_pending()
