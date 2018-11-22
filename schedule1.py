from adScheduler import *

# Setting the schedule settings
ad1 = adSchedule(ad_id=1, repeat=5)
ad1.start()

ad2 = adSchedule(ad_id=2, repeat=3, delay=5)
ad2.start()

while True:
    schedule.run_pending()
