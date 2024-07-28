#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose



class poseSubsNode(Node):

    def __init__(self):
        super().__init__("pose_subs")
        self.pose_subs_ = self.create_subscription( Pose, "/turtle1/pose", self.pose_callback, 10 )
        self.get_logger().info("Pose Subsriber is running")

    def pose_callback(self, msg: Pose):
        self.get_logger().info(f"X: {msg.x}, Y: {msg.y}, Q: {msg.theta} ")




def main(args=None):
    rclpy.init(args=args)
    node  = poseSubsNode()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__=="__main__":
    main()





