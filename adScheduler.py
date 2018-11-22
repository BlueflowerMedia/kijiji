import schedule
import time
import datetime
from adPoster import *

class adSchedule:

    def __init__(self, ad_id, repeat, delay=0):
        self.ad_id = ad_id
        self.repeat = repeat
        self.delay = delay
        self.job_file = "ad" + str(self.ad_id) + "/ad" + str(self.ad_id) + ".yml"

    def printHeader(self):
        logger(str(datetime.datetime.now()))
        logger("AD#" + str(self.ad_id) + " is being reposted every " + str(self.repeat) + " minutes\n")
        logger("AD FILE: " + str(self.job_file) + "\n")

    def printFooter(self, rc):
        if (rc==0):
            logger("No critical errors. Check ADPOSTER OUTPUTS for details")
            logger("=====================================================")
        else:
            logger("There was an error. Check ADPOSTER ERROR for details")
            logger("=====================================================")

    def start(self):
        # delay
        time.sleep(self.delay*60)
        self.printHeader()
        # running the ad first time
        rc = adPoster(self.job_file, repost=False)
        self.printFooter(rc)
        #schedule
        schedule.every(self.repeat).minutes.do(self.repost)

    def repost(self):
        self.printHeader()
        # reposting because repost=True by default [check adPoster]
        rc = adPoster(self.job_file)
        self.printFooter(rc)
