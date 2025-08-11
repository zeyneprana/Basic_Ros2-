#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from  sensor_msgs.msg import LaserScan

class LidarDataNode(Node):
    def __init__(self):
        super().__init__("lidar_data_node")
        self.get_logger().info("Lidar node has been started!")

        self_subscriber_ = self.create_subscription(LaserScan
                                                    "/lidar/out",
                                                     self.callback_data,
                                                      10 )


def callback_data(self,msg):

    min_lidar_data_ = min(msg.ranges)
    self.get_logger().info("LIDAR Data: " + str(min_lidar_data_))

def main(args=None):
    rclpy.init(args=args)
    node = LidarDataNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()