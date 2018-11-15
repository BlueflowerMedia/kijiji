import schedule
import time
import datetime
import testjob

def job12():
    print(datetime.datetime.now())
    ads.job1()
    ads.job2()

def job34():
    print(datetime.datetime.now())
    ads.job3()
    ads.job4()

def job56():
    print(datetime.datetime.now())
    ads.job5()
    ads.job6()

schedule.every(20).minutes.do(job12)
schedule.every(20).minutes.do(job34)
schedule.every(20).minutes.do(job56)

while True:
    schedule.run_pending()
