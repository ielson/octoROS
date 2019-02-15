#!/usr/bin/env python

# import roslib
# roslib.load_manifest('octoROS')

import sys

import rospy
from std_msgs.msg import String

import messenger


class interface:
    def __init__(self):
        self.print_pub = rospy.Publisher('printer3d', String, queue_size=100)

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
            print("Progress: {}%".format(progress))
            # self.print_pub.publish("Progress: {:4:2f}%".format(progress))
        print("Successful print!")
        # self.print_pub.publish("Successful print")


def main(args):
    rospy.init_node('printerWatcher', anonymous=True)
    interf = interface()
    interf.printAndGetStatus('Flexi-Rex-Improved-Maker.gcode')
    rospy.spin()


if __name__ == '__main__':
    main(sys.argv)
