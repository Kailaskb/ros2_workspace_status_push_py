import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('py_pub_spiral_node')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 1)
        timer_period = 0.033  # seconds
        self.linear_velocity = float(sys.argv[1])
        self.angular_velocity_initial = float(sys.argv[2])
        self.angular_velocity_increment = float(sys.argv[3])
        self.i = 0.0
        self.timer_ = self.create_timer(timer_period, self.publish_message)

    def publish_message(self):
        message = Twist()
        message.linear.x = self.linear_velocity + (2 * self.i)
        message.angular.z = self.angular_velocity_initial + self.i
        self.get_logger().info('Sending - Linear Velocity : %f, Angular Velocity : %f' % (message.linear.x, message.angular.z))
        self.publisher_.publish(message)
        self.i += self.angular_velocity_increment

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()