#! /usr/bin/env python


from __future__ import print_function

from beginner_tutorials.srv import GetTime,GetTimeResponse, GetTimeRequest
import rospy
import time


def handle_add_two_ints(req : GetTimeRequest):
    converted = time.localtime(rospy.Time.now().secs)
    formatted = time.strftime( req.format, converted)
    return GetTimeResponse(formatted)

def add_two_ints_server():
    rospy.init_node('get_time_server')
    s = rospy.Service('get_time', GetTime, handle_add_two_ints)
    print("Ready to get time.")
    rospy.spin()


if __name__ == "__main__":
    add_two_ints_server()