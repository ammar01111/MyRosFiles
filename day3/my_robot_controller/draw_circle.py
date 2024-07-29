#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class makeCircle(Node):
    
    def __init__(self):
        super().__init__("draw_my_circle")
        self.circle_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel" ,10)
        self.timer_ = self.create_timer(1.0,self.send_vel_cmd)
        self.get_logger().info("makeCircle Publisher node is running.")

    def send_vel_cmd(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.circle_pub_.publish(msg)

        



def main(args=None):
    rclpy.init(args=args)
    node  = makeCircle()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()