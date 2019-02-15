#!/usr/bin/env python2.7

import requests

octoIP = "http://127.0.0.1"
octoPort = ":5000"
apiKey = "A5B916E2F8724A239572AEB63CA3D682"


standardHeader = {'X-Api-Key': apiKey}


def connectToPrinter():
    connectionData = {"command": "connect", "port": "/dev/ttyACM0", "baudrate": 115200, "printerProfile": "_default",
                      "save": True, "autoconnect": True}
    return requests.post(_url("connection"), json=connectionData, headers=standardHeader, timeout=5)



def modelSelection():
    pass


def printModel(modelName):
    # the modelname with the .gcode
    printData = {'command': 'select', 'print': True}
    url = _url('files/local/{}'.format(modelName))
    return requests.post(url, json=printData, headers=standardHeader, timeout=5)


def progressTracking():
    response = requests.get(_url('job'), headers=standardHeader, timeout=5)
    return (response.json()['progress']['completion'])



def _url(path):
    octoAddress = octoIP + octoPort + '/api/'
    return octoAddress + path
