#!/usr/bin/env python3

from os import system
import requests
import json
from time import sleep

ZABBIX_API_URL = "http://myzabbixurl/zabbix/api_jsonrpc.php"
UNAME = "zabbix_user"
PWORD = "zabbix_psw"

while True:
    sleep(15)        # check every 15 seconds
    r = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "user.login",
                      "params": {
                          "user": UNAME,
                          "password": PWORD},
                      "id": 1
                  })

    AUTHTOKEN = r.json()["result"]

        # Retrieve a list of problems
    r = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "problem.get",
                      "params": {
                          "output": "extend",
                          "selectAcknowledges": "extend",
                          "recent": "true",
                          "sortfield": ["eventid"],
                          "sortorder": "DESC"
                      },
                      "id": 2,
                      "auth": AUTHTOKEN
    })

    #Trigger Baubbix

    for item in r.json()["result"]:
        if (int(item['severity']) >= 4 and item['eventid'] != "1002"):
            system("baubbix.py "+item["name"])
            break
    #End Trigger

    with open('/tmp/zabbixalerts.json','w') as f:
        json.dump(r.json()["result"],f)

        #Logout user
    r = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "user.logout",
                      "params": {},
                      "id": 2,
                      "auth": AUTHTOKEN
                  })