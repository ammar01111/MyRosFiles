#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class turtlesimSubsPubNode(Node):

    def __init__(self):
        super().__init__("turtlesimSUBSpub")
        self.turtlesim_pub_ = self.create_publisher( Twist, "/turtle1/cmd_vel", 10)
        self.turtlesim_subs_ = self.create_subscription( Pose, "/turtle1/pose", self.pose_callback, 10)

    def pose_callback(self, position: Pose):
        send_msg = Twist()
        send_msg.linear.x = 3.0
        if position.x > 9 or position.y > 9 or  position.x < 2 or position.y < 2:
            send_msg.linear.x = 2.0
            send_msg.angular.z = 1.5
        

        self.turtlesim_pub_.publish(send_msg)

        

def main(args = None):
    rclpy.init(args = args)
    node  = turtlesimSubsPubNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

