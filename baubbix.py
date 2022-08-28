#!/usr/bin/env python3

from os import path
from sys import argv
from time import sleep
from requests import post
from datetime import datetime

class CRDog: #Control-Room DOG
    def __init__(self,dog_name,bark_trigger,dog_path_logs='',seconds_barks=3):
        self.dog_logs=path.join(dog_path_logs,dog_name+'.log')
        self.bark = bark_trigger
        self.max_time_barks=seconds_barks
        self.log_format = "BAU at {timestamp} ---- [{trigger_cause}]"
    def dog_trigger(self):
        post('http://mycrdogurl/cm?cmnd=Power%20ON')
    def dog_quiet(self):
        post('http://mycrdogurl/cm?cmnd=Power%20OFF')
    def dog_writer(self):
        with open(self.dog_logs, 'w') as l:
            l.write(self.log_format.format(timestamp=datetime.now(), trigger_cause=self.bark))

if __name__=='__main__':
    try:
        baubbix=CRDog('baubbix',argv[1])
        baubbix.dog_writer()
        #start barking
        baubbix.dog_trigger()
        sleep(baubbix.max_time_barks)
        baubbix.dog_quiet()

    except:
        baubbix = CRDog('baubbix', 'Arguments error')
        baubbix.dog_quiet()
        baubbix.dog_writer()