#!/usr/bin/env python

""" octoROS - integrating octoprint with ROS, so it's possible to control your 3d printer from your robot
This library is based in the octoprint api, more info can be found here:
http://docs.octoprint.org/en/master/api/index.html
"""

import sys

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import String

import messenger


class interface:
    def __init__(self):
        self.print_pub = rospy.Publisher('printer3d', String, queue_size=100)
        self.printFinished_pub = rospy.Publisher('printer3d/finishedPrinting', Bool, queue_size=10)
        self.rate = rospy.Rate(0.1)  # 0.1 hz
        print("initialized")

    def performConnection(self):
        self.print_pub.publish("Trying to connect to 3dprinter")
        connection = messenger.connectToPrinter()
        if connection.status_code != 204:
            # TODO change all exceptions to the right ones
            raise Exception('Could not connect to printer, error code: {}'.format(connection.status_code))
        self.print_pub.publish("Connection Succeed")

    def printAndGetStatus(self, modelName):
        printing = messenger.printModel(modelName)
        if printing.status_code != 204:
            pass
            # raise Exception('Could not print, status code: {}'.format(printing.status_code))
        self.print_pub.publish("Starting to print model {}".format(modelName))
        progress = messenger.progressTracking()
        while progress < 100 and not rospy.is_shutdown():
            progress = messenger.progressTracking()
            print("Progress: {}%".format(progress))
            # TODO change to a action
            self.print_pub.publish("Progress: {}%".format(progress))
            tool0Temp, tool1Temp, bedTemp = messenger.getprinterInfo()
            # TODO Need to see the type returned by getPrinterInfo, so I can make a msg and send it to the right topic
            print("Tool 0 temp: {}C, tool 1 temp: {}C, bed temp: {}C".format(tool0Temp, tool1Temp, bedTemp))
            self.print_pub.publish(
                "Tool 0 temp: {}C, tool 1 temp: {}C, bed temp: {}C".format(tool0Temp, tool1Temp, bedTemp))
            self.rate.sleep()
        print("Successful print!")
        self.print_pub.publish("Successful print")
        self.printFinished_pub.publish(True)


def main(args):
    # Ros was not catching interrupt exceptions, so I had to disable signals and use the KeyboardInterrupt exception
    rospy.init_node('printerWatcher', anonymous=True, disable_signals=True)
    interf = interface()
    interf.printAndGetStatus('FlexiRexColor1.gcode')


if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Shutting down")
        messenger.cancelPrinting()
