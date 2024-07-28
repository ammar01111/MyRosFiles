#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class myNode(Node):

    def __init__(self):
        super().__init__("first_Node")
        self.create_timer(1.0,self.timer_callback)
        self.counter_ = 0
    def timer_callback(self):
        self.get_logger().info(f"Hello {self.counter_}")
        self.counter_ +=1

def main(args = None):
    rclpy.init(args=args)
    node = myNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()