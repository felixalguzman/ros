#!/usr/bin/env python


from __future__ import print_function


import sys
import rospy
from beginner_tutorials.srv import *


def add_two_ints_client(x = None):
    rospy.wait_for_service('get_time')
    try:
        add_two_ints = rospy.ServiceProxy('get_time', GetTime)
        resp1 : GetTimeResponse = add_two_ints(x)
        return resp1.time
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def print_current():
    duration = rospy.Duration(1)
    while(True):
        print(add_two_ints_client())
        rospy.sleep(duration)

def usage():
    return "%s [x]"%sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
        rospy.set_param('format', x)
    else:
        print(usage())
        rospy.set_param('format', r'%D %X')
        # sys.exit(1)
    print("Requesting %s"%(x))
    print_current()
