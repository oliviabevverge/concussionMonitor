import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random
import math

class HelmetSensor(Node):
    def __init__(self):
        super().__init__('helmet_sensor')
        self.pub = self.create_publisher(Float32, 'head_impact', 10)
        self.timer = self.create_timer(0.5, self.publish_impact)
        self.t = 0.0
        self.get_logger().info('🏈 Helmet sensor online — monitoring head impacts...')

    def publish_impact(self):
        # normal motion: low g-force with slight variation
        base = 2.0 + math.sin(self.t) + random.uniform(-0.5, 0.5)

        # ~10% chance of a hit event
        if random.random() < 0.10:
            impact = random.uniform(40.0, 130.0)
            self.get_logger().info(f'💥 HIT detected: {impact:.1f}g')
        else:
            impact = base

        msg = Float32()
        msg.data = float(impact)
        self.pub.publish(msg)
        self.t += 0.1

def main():
    rclpy.init()
    rclpy.spin(HelmetSensor())
    rclpy.shutdown()

if __name__ == '__main__':
    main()