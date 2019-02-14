#!/usr/bin/env python2.7

import requests

octoIP = "127.0.0.1"
octoPort = ":5000"
apiKey = "A5B916E2F8724A239572AEB63CA3D682"

octoAddress = octoIP + octoPort
standardHeader = {'X-Api-Key': apiKey}
connectionData = {"command": "connect", "port": "/dev/ttyACM0", "baudrate": 115200, "printerProfile": "_default",
                  "save": True, "autoconnect": True}


def connectToPrinter():
    connection = requests.post(octoAddress + "/api/connection", json=connectionData, headers=standardHeader)
    if connection.status_code != 201:
        raise ConnectionError("It wasn't possible to connect,  code {}".format(connection.status_code))
    print("Connection successful")


def modelSelection():
    pass


def printModel():
    # o endereço passado deve ser do arquivo .gcode
    printData = {'command': 'select', 'print': True}
    printing = requests.post(octoAddress + '/api/files/local/Flexi-Rex-improved.gcode', json=printData,
                             headers=standardHeader)
    # TODO colocar o if tal codigo raise tal coisa


def progressTracking():


    progress = requests.get(octoAddress + '/api/job', headers=standardHeader)
for item in progress.json():
    print("item: {}".format(item))
