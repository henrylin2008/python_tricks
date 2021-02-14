# In Terminal:
# crontab -l: list of current cron jobs
# crontab -e: open cron job default editor
# echo $EDITOR: check the default editor the system is using
# export EDITOR=nano: change default editor to nano

# crontab - e 
# * * * * * python ~/code/task/test.py: run every minute, run test.py
# * * * * * ~/opt/conda/envs/py38/bin/python ~/code/task/fetch_github.py: run at every minute
#         - ~/opt/conda/envs/py38/bin/python: py38 python environment
#         - ~/code/task/fetch_github.py: run fetch_github.py

# 30 * * * * command: it runs every 30 minutes
# 0 0 * * 1 command: every Monday at midnight 
# 0 0 1,15 * * command: midnight at 1st and 15th 
# */10 * * * * command: every 10 minutes 
# 0 0 */3 * * command: every 3 days 
# 0 0-5 * * * command: every hour from midnight to 5 AM 
# */30 9-17 * * 1-5 command: Monday-Friday, 9am-5pm, every 30 minutes 


# fetch_github.py
import logging
import os
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))  # full path of current directory
filename = os.path.join(dir_path, 'events.log')  # full path + test_log.log; /Users/hlin/code/task/test_log.log

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)


# fetch data from github and log into
def fetch_github_events():
    r = requests.get('https://api.github.com/url')
    events = r.json()
    if events and len(events):
        last_event = events[0]
        logger.info(last_event)
    else:
        logger.error('Could not get last event')


if __name__ == '__main__':
    do_logging()
