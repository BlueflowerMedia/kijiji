# Kijiji Scheduled Reposter

#### Kijiji Scheduled Reposter

## Setup

The project requires python3 with: python-requests, bs4, pyyaml, schedule
To install all dependencies, run:

`pip install -r requirements.txt`
or `pip3 install -r requirements.txt`


## Usage

### Using the script

- Create a folder **ad#** i.e. ad1, ad2
- Place all the photos in the folder
- Create a yml file for the ad in the same name as the folder (either using the CLI the instruction in next section or editing exiting yml file)
- Create a schedule python file. (Look at an example at [schedule1.py](schedule1.py))
  - Start the file with import statement `from adScheduler import *`
  - create a adSchedule class under any variable name with the following parameters
    - ad_id: this must match folder name of the ad yml file and ad yml filename
    - repeat: interval in minutes at which the ad is reposted
    - delay: number of minutes delayed before the ad is started
  - i.e. for ad66 repeated every 30 minutes that will start after 30 minutes:
  `ad1 = adSchedule(ad_id=66, repeat=30, delay=30)`
  - to initiate a schedule, run the start function for each ad. i.e. `ad1.start()`
  - end the file with `while True: schedule.run_pending()`
- to run the script, simply run `python **nameOfTheFile**`


### Creating, Posting and Reposting an ad using the CLI

Create an yml file for an ad using kijiji_repost_headless :

`python kijiji_repost_headless build_ad`

Post one ad (item.yml):

`python kijiji_repost_headless [-u USERNAME] [-p PASSWORD] post myproduct/item.yml`

Repost one ad (item.yml); will delete the ad prior to posting if it already exists:

`python kijiji_repost_headless [-u USERNAME] [-p PASSWORD] repost myproduct/item.yml`

Show all active ads:

`python kijiji_repost_headless [-u USERNAME] [-p PASSWORD] show`

Delete all ads:

`python kijiji_repost_headless [-u USERNAME] [-p PASSWORD] nuke`

Delete one ad (using ad id):

`python kijiji_repost_headless [-u USERNAME] [-p PASSWORD] delete myAdId`
