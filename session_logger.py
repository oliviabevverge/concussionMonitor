import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

class SessionLogger(Node):
    def __init__(self):
        super().__init__('session_logger')
        self.sub = self.create_subscription(String, 'alerts', self.log_alert, 10)
        self.log = []
        self.get_logger().info('Session logger online!')

    def log_alert(self, msg):
        timestamp = datetime.now().strftime('%H:%M:%S')
        entry = f'[{timestamp}] {msg.data}'
        self.log.append(entry)
        print('\n' + '='*60)
        print('  SESSION ALERT LOG')
        print('='*60)
        for event in self.log:
            print(f'  {event}')
        print('='*60 + '\n')

def main():
    rclpy.init()
    rclpy.spin(SessionLogger())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
