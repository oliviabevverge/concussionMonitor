import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

SINGLE_HIT_DANGER = 80.0
CUMULATIVE_WARNING = 300.0

class ImpactMonitor(Node):
    def __init__(self):
        super().__init__('impact_monitor')
        self.sub = self.create_subscription(Float32, 'head_impact', self.analyze, 10)
        self.pub = self.create_publisher(String, 'alerts', 10)
        self.cumulative_g = 0.0
        self.hit_count = 0
        self.get_logger().info('Impact monitor online!')

    def analyze(self, msg):
        g = msg.data
        self.cumulative_g += g
        if g >= SINGLE_HIT_DANGER:
            self.hit_count += 1
            self.get_logger().warn(f'DANGER: {g:.1f}g hit #{self.hit_count} | cumulative: {self.cumulative_g:.1f}g')
            alert = f'DANGER: {g:.1f}g hit #{self.hit_count} | cumulative: {self.cumulative_g:.1f}g'
            self._publish_alert(alert)
        elif self.cumulative_g >= CUMULATIVE_WARNING:
            self.get_logger().warn(f'WARNING: cumulative {self.cumulative_g:.1f}g exceeds limit!')
            self._publish_alert(f'WARNING: cumulative {self.cumulative_g:.1f}g exceeds limit!')
        else:
            self.get_logger().info(f'OK: {g:.1f}g | cumulative: {self.cumulative_g:.1f}g')

    def _publish_alert(self, text):
        msg = String()
        msg.data = text
        self.pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(ImpactMonitor())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
