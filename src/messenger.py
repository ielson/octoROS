#!/usr/bin/env python2.7

""" octoROS - integrating octoprint with ROS, so it's possible to control your 3d printer from your robot
This library is based in the octoprint api, more info can be found here:
http://docs.octoprint.org/en/master/api/index.html
"""


import requests

octoIP = "http://127.0.0.1"
octoPort = ":5000"
apiKey = "A5B916E2F8724A239572AEB63CA3D682"


standardHeader = {'X-Api-Key': apiKey}

# Connection handling
def connectToPrinter():
    connectionData = {"command": "connect", "port": "/dev/ttyACM0", "baudrate": 115200, "printerProfile": "_default",
                      "save": True, "autoconnect": True}
    return requests.post(_url("connection"), json=connectionData, headers=standardHeader, timeout=5)


# File operations
def modelSelection():
    pass


def printModel(modelName):
    # the modelname with the .gcode
    printData = {'command': 'select', 'print': True}
    url = _url('files/local/{}'.format(modelName))
    return requests.post(url, json=printData, headers=standardHeader, timeout=5)


# Job operations
def progressTracking():
    response = requests.get(_url('job'), headers=standardHeader, timeout=5)
    return (response.json()['progress']['completion'])

def cancelPrinting():
    jsonData = {'command':'cancel'}
    return requests.post(_url('job'), headers=standardHeader, timeout=5, json=jsonData)

def pausePrinting():
    jsonData = {'command':'pause', 'action':'pause'}
    return requests.post(_url('job'), headers=standardHeader, timeout=5, json=jsonData)

def resumePrinting():
    jsonData = {'command':'pause', 'action':'resume'}
    return requests.post(_url('job'), headers=standardHeader, timeout=5, json=jsonData)

# Printer operations
def getprinterInfo():
    response = requests.get(_url('printer'), headers=standardHeader, timeout=5)
    tool0Temp = response.json()['temperature']['tool0']['actual']
    tool1Temp = response.json()['temperature']['tool1']['actual']
    bedTemp = response.json()['temperature']['bed']['actual']
    return tool0Temp, tool1Temp, bedTemp


def _url(path):
    octoAddress = octoIP + octoPort + '/api/'
    return octoAddress + path
