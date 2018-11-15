import schedule
import time
import datetime
import testjob

def job1():
    print(datetime.datetime.now())
    print("this is job 1")
    testjob.testjob()


def job2():
    print(datetime.datetime.now())
    print("this is job 2")

schedule.every(1).minutes.do(job1)
schedule.every(2).minutes.do(job2)

while True:
    schedule.run_pending()
