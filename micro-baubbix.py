#baubbix trigger 4 micropython

from time import sleep
from urequests import post
#from datetime import datetime

class CRDog: #Control-Room DOG
    def __init__(self,dog_name,bark_trigger,dog_path_logs='',seconds_barks=3):
        self.dog_logs='' # log disabled into ESP32
        self.bark = bark_trigger
        self.max_time_barks=seconds_barks
        self.log_format = "BAU at {timestamp} ---- [{trigger_cause}]"
    def dog_trigger(self):
        try:
            post('http://mycrdogurl/cm?cmnd=Power%20ON')
        except Exception as error_message:
            print(error_message)
    def dog_quiet(self):
        post('http://mycrdogurl/cm?cmnd=Power%20OFF')
   # def dog_writer(self):
       # with open(self.dog_logs, 'w') as l:
           # l.write(self.log_format.format(timestamp=datetime.now(), trigger_cause=self.bark))


def start_bark_micropython():
    baubbix=CRDog('baubbix','BAU ti ho visto')
    #baubbix.dog_writer()
    baubbix.dog_trigger()
    sleep(baubbix.max_time_barks)
    baubbix.dog_quiet()
